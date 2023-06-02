from adminPanel.forms import MainPageForm, AboutForm, ExperienceForm, EducationForm, LangSkillForm, PortfoliosForm,\
     RecommendationsForm, SocialMediaForm, SEOTagsForm

from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia,\
    userBlog, PIAIC, PIAIC_Notifications, seoTags, MainPage

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def Update(request, id, type):
    if type == 'main_page':
        if request.method =='POST':
            UPMNP = MainPage.objects.get(id=id)
            MNPFM = MainPageForm(request.POST, request.FILES, instance=UPMNP)
            if MNPFM.is_valid():
                MNPFM.save()
                return redirect('/main_page')
        else:
            UPMNP = MainPage.objects.get(id=id)
            MNPFM = MainPageForm(instance=UPMNP)
        return render(request, 'Update/updateMainPage.html', {'form': MNPFM})

    if type == 'about':
        if request.method =='POST':
            UPABT = About.objects.get(id=id)
            ABTFM = AboutForm(request.POST, request.FILES, instance=UPABT)
            if ABTFM.is_valid():
                ABTFM.save()
                return redirect('/about')
        else:
            UPABT = About.objects.get(id=id)
            ABTFM = AboutForm(instance=UPABT)
        return render(request, 'Update/updateAbout.html', {'form': ABTFM})

    if type == 'experience':
        if request.method =='POST':
            UPEXP = Experience.objects.get(id=id)
            EXPFM = ExperienceForm(request.POST, request.FILES, instance=UPEXP)
            if EXPFM.is_valid():
                EXPFM.save()
                return redirect('/experience')
        else:
            UPEXP = Experience.objects.get(id=id)
            EXPFM = ExperienceForm(instance=UPEXP)
        return render(request, 'Update/updateExperience.html', {'form': EXPFM})

    if type == 'education':
        if request.method =='POST':
            UPEDU = Education.objects.get(id=id)
            EDUFM = EducationForm(request.POST, request.FILES, instance=UPEDU)
            if EDUFM.is_valid():
                EDUFM.save()
                return redirect('/education')
        else:
            UPEDU = Education.objects.get(id=id)
            EDUFM = EducationForm(instance=UPEDU)
        return render(request, 'Update/updateEducation.html', {'form': EDUFM})

    if type == 'language_skills':
        if request.method =='POST':
            UPLNSK = LangSkill.objects.get(id=id)
            LNSKFM = LangSkillForm(request.POST, request.FILES, instance=UPLNSK)
            if LNSKFM.is_valid():
                LNSKFM.save()
                return redirect('/languageskills')
        else:
            UPLNSK = LangSkill.objects.get(id=id)
            LNSKFM = LangSkillForm(instance=UPLNSK)
        return render(request, 'Update/updateLanguage_Skills.html', {'form': LNSKFM})

    if type == 'portfolios':
        if request.method =='POST':
            UPPF = Portfolios.objects.get(id=id)
            PFFM = PortfoliosForm(request.POST, request.FILES, instance=UPPF)
            if PFFM.is_valid():
                PFFM.save()
                return redirect('/portfolios')
        else:
            UPPF = Portfolios.objects.get(id=id)
            PFFM = PortfoliosForm(instance=UPPF)
        return render(request, 'Update/updatePortfolios.html', {'form': PFFM})

    if type == 'recommendation':
        if request.method == 'POST':
            UPREC = Recommendations.objects.get(id=id)
            RECFM = RecommendationsForm(request.POST, request.FILES, instance=UPREC)
            if RECFM.is_valid():
                RECFM.save()
                return redirect('/recommendation')
        else:
            UPREC = Recommendations.objects.get(id=id)
            RECFM = RecommendationsForm(instance=UPREC)
        return render(request, 'Update/updateRecommendations.html', {'form': RECFM})

    if type == 'socialMedia':
        if request.method == 'POST':
            UPSM = SocialMedia.objects.get(sNo=id)
            SMFM = SocialMediaForm(request.POST, request.FILES, instance=UPSM)
            if SMFM.is_valid():
                SMFM.save()
                return redirect('/socialMedia')
        else:
            UPSM = SocialMedia.objects.get(sNo=id)
            SMFM = SocialMediaForm(instance=UPSM)
        return render(request, 'Update/updateSocialMedia.html', {'form': SMFM})

    if type == 'blog':

        UpdateForm = userBlog.objects.get(sNo=id)
        if request.method == 'POST':
            file_data = request.POST.get('edit_file')
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.quote = request.POST.get('quote')
            UpdateForm.quote_by = request.POST.get('quote_by')
            UpdateForm.description = request.POST.get('editor1')
            if not file_data == 'False':
                UpdateForm.Icon = request.FILES['icon']
            UpdateForm.save()
            return redirect('/adminblog')

        return render(request, 'Update/updateBlog.html', {'form': UpdateForm})

    if type == 'piaic_notification':

        UpdateForm = PIAIC_Notifications.objects.get(sNo=id)
        if request.method == 'POST':
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.instructions = request.POST.get('instructions')
            UpdateForm.instructions_By = request.POST.get('instructions_By')
            UpdateForm.description = request.POST.get('editor1')
            UpdateForm.save()
            return redirect('/adminPIAIC_Notifications')

        return render(request, 'Update/adminUpdateNotification.html', {'form': UpdateForm})

    if type == 'piaic_admin':

        UpdateForm = PIAIC.objects.get(sNo=id)
        if request.method == 'POST':
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.instructions = request.POST.get('instructions')
            UpdateForm.instructions_By = request.POST.get('instructions_By')
            UpdateForm.description = request.POST.get('editor1')
            UpdateForm.save()
            return redirect('/adminPIAIC')

        return render(request, 'Update/updateadminPIAIC.html', {'form': UpdateForm})

    if type == 'seoTags':
        if request.method == 'POST':
            UpdateRecord = seoTags.objects.get(id=id)
            UpdateForm = SEOTagsForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/seotags')
        else:
            UpdateRecord = seoTags.objects.get(id=id)
            UpdateForm = SEOTagsForm(instance=UpdateRecord)
        return render(request, 'Update/UpdateSEOTags.html', {'form': UpdateForm})
