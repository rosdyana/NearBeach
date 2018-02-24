"""
VIEWS - project information
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This views python file will store all the required classes/functions for the AJAX
components of the PROJECT INFORMATION MODULES. This is to help keep the VIEWS
file clean from AJAX (spray and wipe).
"""

from django.contrib.auth.decorators import login_required
from .models import *
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import  loader
from NearBeach.forms import *
from .models import *
from .misc_functions import *

import simplejson
from .user_permissions import return_user_permission_level
from django.urls import reverse


@login_required(login_url='login')
def information_customer_contact_history(request, customer_id):
    customer_permissions = 0
    contact_history_perm = 0

    if request.session['is_superuser'] == True:
        customer_permissions = 4
        contact_history_perm = 4
    else:
        pp_results = return_user_permission_level(request, None,'customer')
        ph_results = return_user_permission_level(request, None, 'contact_history')

        if pp_results > customer_permissions :
            customer_permissions = pp_results

        if ph_results == 1:
            contact_history_perm = 1

    if customer_permissions  == 0:
        return HttpResponseRedirect(reverse('permission_denied'))

    if request.method == "POST":
        # Save everything!
        form = information_customer_contact_history_form(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            """
            If the user has written something in the contact section, we want to save it
            """
            contact_history_notes = form.cleaned_data['contact_history']
            print(contact_history_notes)

            if not contact_history_notes == '':
                # Lets save some contact history
                contact_type = form.cleaned_data['contact_type']

                contact_date = convert_to_utc(
                    int(form.cleaned_data['start_date_year']),
                    int(form.cleaned_data['start_date_month']),
                    int(form.cleaned_data['start_date_day']),
                    int(form.cleaned_data['start_date_hour']),
                    int(form.cleaned_data['start_date_minute']),
                    form.cleaned_data['start_date_meridiems']
                )

                """
                        document_save = documents(
            document_description=filename,
            document=file,
            change_user=request.user,
        )
        document_save.save()

        document_permissions_save = document_permissions(
            document_key=document_save,
            change_user=request.user,
        )
        if project_or_task == "P":
            #Project
            project_instance = project.objects.get(project_id=location_id)
            document_permissions_save.project_id = project_instance
        else:
            #Task
            task_instance = tasks.objects.get(tasks_id=location_id)
            document_permissions_save.task_id = task_instance
document_permissions_save.save()
"""


                # documents
                contact_attachment = request.FILES.get('contact_attachment')
                if contact_attachment:
                    documents_save = documents(
                        document_description=contact_attachment,
                        document=contact_attachment,
                        change_user=request.user,
                    )
                    documents_save.save()

                    # Add to document permissions
                    document_permissions_save = document_permissions(
                        document_key=documents_save,
                        customer_id=customers.objects.get(customer_id=customer_id),
                        change_user=request.user,
                    )
                    document_permissions_save.save()

                customer_instance = customers.objects.get(customer_id=customer_id)

                submit_history = contact_history(
                    organisations_id=customer_instance.organisations_id,
                    customer_id=customer_instance,
                    contact_type=contact_type,
                    contact_date=contact_date,
                    contact_history=contact_history_notes,
                    user_id=current_user,
                    change_user=request.user,
                    document_key=documents_save,
                )
                if contact_attachment:
                    submit_history.document_key = documents_save
                submit_history.save()



    #Data
    customer_contact_history = contact_history.objects.filter(
        customer_id=customers.objects.get(customer_id=customer_id)
    )

    contact_date = datetime.datetime.now()

    #Load template
    t = loader.get_template('NearBeach/customer_information/customer_contact_history.html')

    # context
    c = {
        'contact_history_form': information_customer_contact_history_form(),
        'customer_contact_history': customer_contact_history,
        'media_url': settings.MEDIA_URL,
        'PRIVATE_MEDIA_URL': settings.PRIVATE_MEDIA_URL,
        'contact_year': contact_date.year,
        'contact_month': contact_date.month,
        'contact_day': contact_date.day,
        'contact_hour': contact_date.hour,
        'contact_minute': int(contact_date.minute/5)*5,
        'contact_history_perm': contact_history_perm,
        'customer_permissions': customer_permissions,
    }

    return HttpResponse(t.render(c, request))


@login_required(login_url='login')
def information_customer_documents_list(request, customer_id, organisations_id=''):
    customer_permissions = 0
    document_perm = 0

    if request.session['is_superuser'] == True:
        customer_permissions = 4
        document_perm = 4
    else:
        pp_results = return_user_permission_level(request, None,'customer')
        ph_results = return_user_permission_level(request, None, 'documents')

        if pp_results > customer_permissions:
            customer_permissions = pp_results

        if ph_results == 1:
            document_perm = 1

    if customer_permissions == 0:
        return HttpResponseRedirect(reverse('permission_denied'))


    #Get Data
    customer_document_results = document_permissions.objects.filter(
        customer_id=customer_id,
        is_deleted="FALSE",
    )
    try:
        organisation_document_results = document_permissions.objects.filter(
            organisations_id=organisations_id,
            customer_id__isnull=True,
            is_deleted="FALSE",
        )
    except:
        organisation_document_results = None


    #Load template
    t = loader.get_template('NearBeach/customer_information/customer_documents_list.html')

    # context
    c = {
        'customer_id': customer_id,
        'customer_document_results': customer_document_results,
        'organisation_document_results': organisation_document_results,
        'customer_permissions': customer_permissions,
        'document_perm': document_perm,
    }

    return HttpResponse(t.render(c, request))


@login_required(login_url='login')
def information_customer_documents_upload(request, customer_id):
    if request.method == "POST":
        if request.FILES == None:
            return HttpResponseBadRequest('File needs to be uploaded')

        #Get the file data
        file = request.FILES['file']

        #Data objects required
        filename = str(file)
        file_size = file._size
        print("File name: " + filename + "\nFile Size: " + str(file_size))

        """
        File Uploads
        """
        customer_results = customers.objects.get(customer_id=customer_id)
        document_save = documents(
            document_description=filename,
            document=file,
            change_user=request.user,
        )
        document_save.save()

        document_permissions_save = document_permissions(
            document_key=document_save,
            organisations_id=customer_results.organisations_id,
            customer_id=customer_results,
            change_user=request.user,
        )
        document_permissions_save.save()

        result = []
        result.append({
            "name" : filename,
            "size" : file_size,
            "url" : '',
            "thumbnail_url" : '',
            "delete_url" : '/',
            "delete_type" : "POST",
        })
        response_data = simplejson.dumps(result)
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponseBadRequest('Only POST accepted')
