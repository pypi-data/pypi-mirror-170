# Django Onepage Application

## Project description

Django Onepage is set of functionality that can help you to convert your django application to onepage application. 
These include table listing for every model under respective module, hierarchical navbar for module and model management, 
Onepage add, change, delete operations without page loading with good interaction.


## Settings

Django Onepage is a package that can reduce your page loading by 90%++, Just need to install the package, 
add package to your settings INSTALLED_APPS and update TEMPLATES tag to APP_DIRS is True

    INSTALLED_APPS = [
        ...
        'onepage',
        '''
    ]

    TEMPLATES = [
        {
            ...
            'APP_DIRS': True,
            ...
        },
    ]


## Add Model to Onepage Pattern

Add pattern for your model in any urls file, that can map your model for Onepage CRUD.
we suggest to use django ModelForm instead of django Form for add and change entry.
See django model form documentation to know more about django form binding for model.
We use this forms to add and change database entry from your onepage table, example bellow,
    
    # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

    from onepage.urls import patterns, add_pattern
    from .models import Book, Consumer
    from .forms import BookAddUpdateForm, ConsumerAddForm, ConsumerUpdateForm

    # If you don't pass any form for change entry, form for add entry will be execute for change entry
    # You can pass a validator optionally to check in every action from onepage

    # add_pattern(model_name, form_for_add_entry, form_for_change_entry, validator)

    add_pattern(Book, BookAddUpdateForm)
    add_pattern(Consumer, ConsumerAddForm, ConsumerUpdateForm)

    urlpatterns = [
        ...
    ] + patterns


## Add Pattern to your template

In your base template include onepage/nav.html or you can use onepage/base.html also to get job done.
This nav will generate and give you basic navbar to click and enjoy the simplicity.

In your base template include nav file as like

    {% include 'onepage/nav.html' %}

Or you can simply use onepage base template, it will include your nav.html also

    {% include 'onepage/base.html' %}


## Custom Navigation & Links

If you don't want to add onepage rendered navigation bar through onepage/nav.html, you can right custom
navigation and links to handle onepage application. Let's look at the topic below to more about this.

here {{module_name}} is your app name which containing your desired model, and model_name is your 
desired model name, which you want to initialize.

### View Reference

View reference like admin panel CRUD for model can be created by doing this,

    <li id="{{module_name}}-view-{{model_name}}" class="ajax-four-act-handler"
        data-props="{{module_name}}-view-{{model_name}}" data-r-kwargs="" data-keys="id,field_1,field_2"
    >Model Verbose Name</li>

### Create Reference

Create reference for getting executed and show a create window for model,

    <button data-props="{{module_name}}-add-{{model_name}}"
        class="btn btn-info-soft w-100p mb-2 me-1 ajax-four-act-handler-call-add-change-{{model_name}}"
    >Add New {{model_name}}</button>

### Update Reference

Update reference for getting executed and show an edit window for model, you have to 
follow a hierarchical guidelines.

    <tr data-id="{{ item_id }}">
        <a data-method="GET"
            class="btn btn-success-soft btn-sm ajax-four-act-handler-call-add-change-{{model_name}}" 
             data-props="{{module_name}}-change-{{model_name}}"
        >Edit</a>
    </tr>

### Delete Reference

Delete reference for getting executed, also have to follow a hierarchical guidelines.

    <tr data-id="{{ item_id }}">
        <a data-method="GET"
           class="btn btn-danger-soft btn-sm ajax-four-act-handler-call-add-change-{{model_name}}"
            data-props="{{module_name}}-delete-{{model_name}}"
        >Delete</a>
    </tr>

## Validator

Validator is used to validate query request from user, when you pass any validator to add_pattern.
This validator will be called in view function for add, change, view, delete.


    from onepage.validator import BasicValidator

    class CustomValidator(BasicValidator):
        def is_valid(self):
            return False

    add_pattern(Book, BookAddUpdateForm, validator=CustomValidator)


## Author

django-onepage is an open source library for Python.
Initially developed by Nj Nafir [Nj Nafir Github](https://github.com/njNafir)


## Contribute
- Issue Tracker: [django-onepage Issues](https://github.com/njNafir/django-onepage/issues)
- Source Code: [django-onepage Sources](https://github.com/njNafir/django-onepage)


## Support

If you are having issues, please let us know.
We have a mailing list located at: njnafir@gmail.com


## License
The project licensed under the MIT license.
