from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from CommitteApp.models import *
from CommitteApp.forms import *
# Create your views here.
def branch_categories(request):
    branch_categories = BranchCategory.objects.all()
    context = {'branch_categories': branch_categories}
    return render(request, 'committee/branch_categories.html', context)
    
def branch_categories_form(request):
    if request.method == 'POST':
        form = BranchCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch category name has been added successfully')
            return redirect('branch_categories')
    else:
        form = BranchCategoryForm()
        context = {'form': form,}
    return render(request, 'committee/branch_categories_form.html', context)

def branch_categories_updated(request, slug, pk):
    branch_categories = get_object_or_404(BranchCategory, slug=slug, pk=pk)
    if request.method == 'POST':
        form = BranchCategoryForm(request.POST, instance=branch_categories)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch name has been updated successfully')
            return redirect('branch_categories')
    else:
        form = BranchCategoryForm(instance=branch_categories)
        context = {'form': form,} 
    return render(request, 'committee/branch_categories_form.html', context)


def branch_categories_delete(request, slug, pk):
    branch_categories = get_object_or_404(BranchCategory, slug=slug, pk=pk)
    branch_categories.delete()
    return redirect('branch_categories')


def branch_name(request, slug, pk):
   branch_categories =BranchCategory.objects.get(slug=slug, pk=pk)
   branch_name = BranchName.objects.all().filter(branch_category=branch_categories)
   context = {'branch_name': branch_name, 'branch_categories': branch_categories}
   return render(request, 'committee/branch_name.html', context)

def branch_name_form(request, slug, pk):
    branch_categories =BranchCategory.objects.get(slug=slug, pk=pk)
    if request.method == 'POST':
        form = BranchNameForm(request.POST)
        if form.is_valid():
            branch_name = form.save(commit=False)
            branch_name.branch_category = branch_categories
            branch_name.save()
            messages.info(request, 'branch year has been added successfully')
            return HttpResponseRedirect(reverse('branch_name', args=(branch_categories.slug, branch_categories.pk,)))
    else:
        form = BranchNameForm()
        context = {'form': form, 'branch_categories': branch_categories,}
    return render(request, 'committee/branch_name_form.html', context)

def branch_name_update(request, slug, pk):
    branch_name =get_object_or_404(BranchName, slug=slug, pk=pk)
    if request.method == 'POST':
        form = BranchNameForm(request.POST, instance=branch_name)
        if form.is_valid():
            form.save()
            messages.info(request, 'branch year has been updated successfully')
            return HttpResponseRedirect(reverse('branch_name', args=(branch_name.branch_category.slug, branch_name.branch_category.pk,)))
            # return redirect('branch_name')
    else:
        form = BranchNameForm(instance=branch_name)
        context = {'form': form, 'branch_name': branch_name,}
    return render(request, 'committee/branch_name_form.html', context)

def branch_name_delete(request, slug, pk):
    branch_name = get_object_or_404(BranchName, slug=slug, pk=pk)
    branch_name.delete()
    return HttpResponseRedirect(reverse('branch_name', args=(branch_name.branch_category.slug, branch_name.branch_category.pk,)))


def branch_year_list(request, slug, pk):
    branch_name = BranchName.objects.get(slug=slug, pk=pk)
    branch_years = BranchYear.objects.all().filter(branches=branch_name)
    context = {'branch_name': branch_name , 'branchyears': branch_years}
    return render(request, 'committee/branch_year.html', context )


def branch_year_create_form(request, slug, pk):
    branch_name = BranchName.objects.get(slug=slug, pk=pk)
    if request.method == 'POST':
        form = BranchYearForm(request.POST)
        if form.is_valid():
            form_year = form.save(commit=False)
            form_year.branches = branch_name
            form_year.save()
            messages.info(request, 'branch year has been added successfully')
            return HttpResponseRedirect(reverse('branch_year_list', args=(branch_name.slug, branch_name.pk,)))
    else:
        form = BranchYearForm()
        context = {'form': form, 'branch_name': branch_name,}
    return render(request, 'committee/branch_year_form.html', context)


def branch_year_update(request, slug, pk):
    branch_years = get_object_or_404(BranchYear, slug=slug, pk=pk)
    if request.method == 'POST':
        form = BranchYearForm(request.POST, instance=branch_years)
        if form.is_valid():
            form.save()
            messages.info(request, 'branch year has been updated successfully')
            return HttpResponseRedirect(reverse('branch_year_list', args=(branch_years.branches.slug, branch_years.branches.pk,)))
            # return redirect('branch_name')
    else:
        form = BranchYearForm(instance=branch_years)
        context = {'form': form, 'branch_years': branch_years,}
    return render(request, 'committee/branch_year_form.html', context)

def branch_year_delete(request, slug, pk):
    branch_years = get_object_or_404(BranchYear, slug=slug, pk=pk)
    branch_years.delete()
    return HttpResponseRedirect(reverse('branch_year_list', args=(branch_years.branches.slug, branch_years.branches.pk,)))

def branch_member(request, slug, pk):
    branch_years = BranchYear.objects.get(slug=slug, pk=pk)
    members = BranchMember.objects.filter(branch_year=branch_years)
    context = { 'members': members, 'branch_years': branch_years}
    return render(request, 'committee/branch_member.html', context)


def add_member_form(request, slug, pk):
    branch_years = BranchYear.objects.get(slug=slug, pk=pk)
    if request.method == 'POST':
        form = MemberAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.branch_year = branch_years
            obj.save()
            messages.info(request, 'Branch leader has been added successfully')
            return HttpResponseRedirect(reverse('branch_member', args=(branch_years.slug, branch_years.pk,)))
    else:
        form = MemberAddForm()
        context = { 'form': form, 'branch_years': branch_years}
    return render(request, 'committee/branch_member_form.html', context)

def member_details_update(request, slug, pk):
    member = get_object_or_404(BranchMember, slug=slug, pk=pk)
    form = MemberAddForm(instance=member)
    if request.method == 'POST':
        form = MemberAddForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch leader has been updated successfully')
            return HttpResponseRedirect(reverse('branch_member', args=(member.branch_year.slug, member.branch_year.pk,)))
    else:
        form = MemberAddForm(instance=member)
    context = { 'form': form,}
    return render(request, 'Leader_app/add_member_form.html', context)

def branch_member_delete(request, slug, pk):
    member = get_object_or_404(BranchMember, slug=slug, pk=pk)
    member.delete()
    return HttpResponseRedirect(reverse('branch_member', args=(member.branch_year.slug, member.branch_year.pk,)))

def branch_leader_details(request, slug, pk):
    Branchdetail = get_object_or_404(BranchMember, slug=slug, pk=pk)
    context = {'Branchdetail': Branchdetail}
    return render(request, 'committee/branch_leader_details.html', context)


# central leader fuctions


def central_years(request):
    years = CentralYear.objects.order_by('-id')
    context = { 'years': years}
    return render(request, 'committee/central_leader/session_central.html', context )

def central_year_form(request):
    if request.method == 'POST':
        form = CentralForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Central year has been added successfully')
            return redirect('central_years')
    else:
        form = CentralForm()
    return render(request, 'committee/central_leader/centralyear_form.html', context={'form': form,})


def central_year_update(request, slug, pk):
    central_year = get_object_or_404(CentralYear, slug=slug, pk=pk)
    if request.method == 'POST':
        form = CentralForm(request.POST, instance=central_year)
        if form.is_valid():
            form.save()
            messages.info(request, 'Central year has been updated successfully')
            return redirect('central_years')
    else:
        form = CentralForm(instance=central_year)
    return render(request, 'committee/central_leader/centralyear_form.html',
     context={'form': form })

def central_year_delete(request, slug, pk):
    central_year = get_object_or_404(CentralYear, slug=slug, pk=pk)
    central_year.delete()
    return redirect('central_years')

def central_leader(request, slug, pk):
    central_year = CentralYear.objects.get(slug=slug, pk=pk)
    centralLeader = CentralMember.objects.all().filter(session__exact=central_year)
    context = {'central_year': central_year, 'centralLeader': centralLeader}
    return render(request, 'committee/central_leader/central_leader.html', context)

def central_member_form(request, slug, pk):
    central_year = CentralYear.objects.get(slug=slug, pk=pk)
    if request.method == 'POST':
        form = CentralMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form_year = form.save(commit=False)
            form_year.session = central_year
            form_year.save()
            messages.info(request, 'Central leader has been added successfully')
            return HttpResponseRedirect(reverse('central_leader', args=(central_year.slug, central_year.pk,)))
    else:
        form = CentralMemberForm()
        context = {'form': form, 'central_year': central_year}
    return render(request, 'committee/central_leader/central_member_form.html', context)



def central_leader_details(request, slug, pk):
    centraldetail = get_object_or_404(CentralMember, slug=slug, pk=pk)
    context = {'centraldetail': centraldetail}
    return render(request, 'committee/central_leader/central_leader_details.html', context)

def central_leader_update(request, slug, pk):
    central_leader = get_object_or_404(CentralMember, slug=slug, pk=pk)
    form = CentralMemberForm(instance=central_leader)
    if request.method == 'POST':
        form = CentralMemberForm(request.POST, request.FILES, instance=central_leader)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch leader has been updated successfully')
            return HttpResponseRedirect(reverse('central_leader', args=(central_leader.session.slug, central_leader.session.pk,)))
    else:
        form = CentralMemberForm(instance=central_leader)
    context = {'form': form, 'central_leader': central_leader}
    return render(request, 'committee/central_leader/central_member_form.html', context)

def central_leader_delete(request, slug, pk):
    central_leader = get_object_or_404(CentralMember, slug=slug, pk=pk)
    central_leader.delete()
    return redirect('central_years')

def co_ordinator_list(request):
    coordinators = Coordinator.objects.all()
    context = {'coordinators': coordinators}
    return render(request, 'committee/co-ordinator/co_ordinator.html', context )

def co_ordinator_details(request, slug, pk):
    Coordinatordetail = get_object_or_404(Coordinator, slug=slug, pk=pk)
    context = {'Coordinatordetail': Coordinatordetail}
    return render(request, 'committee/co-ordinator/co_ordinator_details.html', context)

def coordinator_create(request):
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'co-ordinator has been added successfully')
            return redirect('co_ordinator_list')
    else:
        form = CoordinatorForm()
        context = {'form': form,}
    return render(request, 'committee/co-ordinator/coodinator_create_form.html', context)

def coordinator_update(request, slug, pk):
    co_ordinator = get_object_or_404(Coordinator, slug=slug, pk=pk)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, request.FILES, instance=co_ordinator)
        if form.is_valid():
            form.save()
            messages.info(request, 'co-ordinator has been updated successfully')
            return redirect('co_ordinator')
    else:
        form = CoordinatorForm(instance=co_ordinator)
        context = {'form': form,}
    return render(request, 'committee/co-ordinator/coodinator_create_form.html', context)


def co_ordinator_delete(request, slug, pk):
    co_ordinator = get_object_or_404(Coordinator, slug=slug, pk=pk)
    co_ordinator.delete()
    return redirect('co_ordinator')
