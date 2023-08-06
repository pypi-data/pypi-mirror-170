from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .utils import *
import json

set_gv()


def onepage_home(request):
    try:
        base_html_file = settings.ONEPAGE_BASE_HTML
    except:
        base_html_file = 'onepage/base.html'

    return render(request, base_html_file)


def ajax_two_act_handler(request):
    data, files = populate_data_from_request(request)
    app_label, action, model_name = model_props(
        data.get('model-props', 'auth-add-group')
    )

    response = check_act_perm(
        request, app_label, action, model_name
    )

    if response:
        return response

    method = request.method

    try:
        validate = False
        validator = gv.validator_map.get(model_name, False)

        if validator:
            validate = validator().is_valid()

        if not validate:
            raise Exception('Request not allowed, please check permission.')

        if method == 'POST' and action == 'add':
            form = gv.ajax_form_map[data['model-props']](
                request.POST, request.FILES, user=request.user
            )

            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors.as_text())

        elif method == 'POST' and action == 'change':
            data['r_kwargs'] = "id=%s" % data['pk']

            form = gv.ajax_form_map[data['model-props']](
                request.POST, request.FILES, instance=get_instance_by_kwargs(
                    data, model_name=model_name, request_user=request.user
                ).first())

            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors.as_text())
        else:
            raise Exception('Request and action is not valid.')

    except Exception as e:
        data['error'] = str(e)

    if request.is_ajax():
        response = JsonResponse(data)

        if data.get('error', False):
            response.status_code = 403

        return response


def ajax_four_act_handler(request, props=None):
    url_hit = True

    if props is None:
        data, files = populate_data_from_request(request)
        url_hit = False
    else:
        data = gv.data_map_for_list_view.get(props, False)
        if type(data) is dict:
            data['model-props'] = props
        else:
            return HttpResponse('')

    try:
        data_props = data.get('model-props', 'auth-add-group')
        app_label, action, model_name = model_props(data_props)

        if not url_hit:
            session_model_kw = request.session.get('session-model-kw')

            if session_model_kw:
                this_model_kw = session_model_kw.get(data_props, False)

                if this_model_kw:
                    for key, value in this_model_kw.items():
                        if data.get(key, "") != value:
                            raise Exception("Request not valid, try again.", )

        response = check_act_perm(
            request, app_label, action, model_name
        )

        if response:
            return response

        method = request.method
        data['verbose_name'] = get_verbose_name(model_name)

        if method == 'GET' and action == 'view':
            result = {'action': 'view'}
            keys = data.get('data-keys')

            try:
                base_html_file = settings.ONEPAGE_BASE_HTML
            except:
                base_html_file = 'onepage/base.html'

            if keys and keys != '':
                keys = keys.split(',')
            else:
                keys = gv.data_map_for_list_view[app_label + '-' + 'view' + '-' + model_name]['data-keys'].split(',')

            replace_fields = gv.replace_fields[model_name]

            if replace_fields:
                for key, value in replace_fields.items():

                    if key in keys:
                        ind = keys.index(key)
                        keys[ind] = value

            data['data_add_props'] = app_label + '-add-' + model_name
            data['data_change_props'] = app_label + '-change-' + model_name
            data['data_delete_props'] = app_label + '-delete-' + model_name

            data['add_perm'] = request.user.has_perm(
                app_label + '.' + 'add' + '_' + model_name
            )
            data['change_perm'] = request.user.has_perm(
                app_label + '.' + 'change' + '_' + model_name
            )
            data['delete_perm'] = request.user.has_perm(
                app_label + '.' + 'delete' + '_' + model_name
            )

            data['ajax_call_add_change'] = 'ajax-four-act-handler-call-add-change-' + model_name
            data['custom_script'] = get_form_call_custom_script(
                data['ajax_call_add_change'],
                gv.scripts_map[model_name].get('view', '')
            )

            if url_hit:
                data['custom_script'] = data['custom_script'] + """
                    $('#dataTableDynamics').DataTable({dom: 'Bfrtip', buttons: ['copy', 'csv', 'excel', 'pdf', 'print', 'colvis']});
                """

            data['objects'] = list(get_instance_by_kwargs(
                data, model_name=model_name, request_user=request.user
            ).values(*keys).all())

            data['headers'] = get_verbose_name_for_fields(model_name, keys)

            result['html'] = get_template('onepage/list.html').render(
                data, request=request
            )

            if request.is_ajax():
                return JsonResponse(result)
            else:
                return render(request, base_html_file, {
                    'html_body': result['html']
                })

        elif method == 'GET' and action == 'add':
            result = {'action': 'add'}

            form = gv.ajax_form_map[data['model-props']](user=request.user)

            class_name = 'ajax-four-act-handler-add-' + model_name
            data['custom_script'] = get_custom_script(class_name, gv.scripts_map[model_name].get('add', ''))
            data['form_props'] = app_label + '-add-' + model_name
            data['method'] = 'POST'

            result['html'] = get_template('onepage/form.html').render(
                populate_template_context(
                    form, data, class_name
                ), request=request
            )

            return JsonResponse(result)

        elif method == 'GET' and action == 'change':
            result = {'action': 'change'}
            data['r_kwargs'] = "id=%s" % data['id']

            form = gv.ajax_form_map[data['model-props']](
                instance=get_instance_by_kwargs(
                    data, model_name=model_name, request_user=request.user
                ).first())

            class_name = 'ajax-four-act-handler-change-%s-%s' % (
                model_name, data.get('id', 0)
            )
            data['custom_script'] = get_custom_script(class_name, gv.scripts_map[model_name].get('change', ''))
            data['form_props'] = app_label + '-change-' + model_name
            data['method'] = 'POST'

            result['html'] = get_template('onepage/form-edit.html').render(
                populate_template_context(
                    form, data, class_name
                ), request=request
            )

            return JsonResponse(result)

        elif method == 'GET' and action == 'delete':
            result = {'action': 'delete'}
            data['r_kwargs'] = "id=%s" % data['id']

            instance = get_instance_by_kwargs(
                data, model_name=model_name, request_user=request.user
            ).first()

            instance.delete()

            return JsonResponse(result)

        else:
            response = JsonResponse(
                {'message': 'Request and action is not valid.'}
            )
            response.status_code = 403

            return response

    except Exception as error:
        response = JsonResponse(
            {'message': str(error)}
        )
        response.status_code = 403
    
        return response


def onepage_set_session(request):
    try:
        data = json.loads(request.GET['body'])

        if request.is_ajax():
            request.session['session-model-kw'] = data
            return JsonResponse(data)
        else:
            raise Exception('Method not allowed.')

    except Exception as e:
        if request.is_ajax():
            err = {
                'error': str(e)
            }
    
            response = JsonResponse(err)
            response.status_code = 403
    
            return response
