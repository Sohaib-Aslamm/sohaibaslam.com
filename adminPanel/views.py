from adminPanel.forms import AboutForm, ExperienceForm, EducationForm, LangSkillForm, PortfoliosForm,\
    RecommendationsForm, SocialMediaForm, UserForm

from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia,\
hello, userBlog, blog_Review, PIAIC, PIAIC_Attachments, PIAIC_Notifications, PIAIC_ICONS

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from adminPanel.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login as auth_login, logout




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Auth Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        URFM = UserForm(request.POST, request.FILES)
        if URFM.is_valid():
            URFM.save()
            user = URFM.cleaned_data.get('username')
            messages.success(request, f'Hey !  {user} your account created successfully')
            return redirect('/user_login')
    else:
        URFM = UserForm()
    return render(request, 'User_Register.html', {'form': URFM})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f'Welcome to your portfolio {user}')
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out !')
    return redirect('/user_login')


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Insert Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
def adminHome(request):
    my_messages = hello.objects.all()
    return render(request, 'HomeAdmin.html', {'my_messages': my_messages})


@login_required(login_url='/user_login')
def viewMessage(request, id):
    messages_detail = hello.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})


@login_required(login_url='/user_login')
def adminAbout(request):
    if request.method == 'POST':
        ABFM = AboutForm(request.POST, request.FILES)
        if ABFM.is_valid():
            FN = ABFM.cleaned_data['fullName']
            DSG = ABFM.cleaned_data['Designation']
            STR = ABFM.cleaned_data['street']
            AOR = ABFM.cleaned_data['areaofResearch']
            PJ = ABFM.cleaned_data['previousJob']
            SCH = ABFM.cleaned_data['School']
            NAT = ABFM.cleaned_data['Nationality']
            MS = ABFM.cleaned_data['meritalStatus']
            BD = ABFM.cleaned_data['Birthday']
            SK = ABFM.cleaned_data['Skype']
            EM = ABFM.cleaned_data['Email']
            PH = ABFM.cleaned_data['Phone']
            DSC = ABFM.cleaned_data['description']
            RSM = ABFM.cleaned_data['resume']
            PR = ABFM.cleaned_data['profile']
            reg = About(fullName=FN, Designation=DSG, street=STR, areaofResearch=AOR, previousJob=PJ,
                        School=SCH, Nationality=NAT, meritalStatus=MS, Birthday=BD, Skype=SK,
                        Email=EM, Phone=PH, description=DSC, resume=RSM, profile=PR)
            reg.save()
            ABFM = AboutForm()
    else:
        ABFM = AboutForm()
    ABTMD = About.objects.all()
    return render(request, 'adminAbout.html', {'form': ABFM, 'ABTMD': ABTMD})


@login_required(login_url='/user_login')
def adminExperience(request):
    if request.method == 'POST':
        EXPFM = ExperienceForm(request.POST, request.FILES)
        if EXPFM.is_valid():
            DSG = EXPFM.cleaned_data['Designation']
            FRM = EXPFM.cleaned_data['From']
            TO = EXPFM.cleaned_data['To']
            CMP = EXPFM.cleaned_data['Company']
            STR = EXPFM.cleaned_data['Street']
            DESC = EXPFM.cleaned_data['Description']
            reg = Experience(Designation=DSG, From=FRM, To=TO, Company=CMP, Street=STR,
                             Description=DESC)
            reg.save()
            EXPFM = ExperienceForm()
    else:
        EXPFM = ExperienceForm()
    data = Experience.objects.all()
    return render(request, 'adminExperience.html', {'form': EXPFM, 'EXPdata': data})


@login_required(login_url='/user_login')
def adminEducation(request):
    if request.method == 'POST':
        EDUFM = EducationForm(request.POST, request.FILES)
        if EDUFM.is_valid():
            SC = EDUFM.cleaned_data['School']
            SA = EDUFM.cleaned_data['StudyArea']
            FRM = EDUFM.cleaned_data['From']
            TO = EDUFM.cleaned_data['To']
            EI = EDUFM.cleaned_data['Icon']
            reg = Education(School=SC, From=FRM, To=TO, StudyArea=SA, Icon=EI)
            reg.save()
            EDUFM = EducationForm()
    else:
        EDUFM = EducationForm()
    data = Education.objects.all()
    return render(request, 'adminEducation.html', {'form': EDUFM, 'EDUdata': data})


@login_required(login_url='/user_login')
def SkillsLang(request):
    if request.method == 'POST':
        SLFM = LangSkillForm(request.POST, request.FILES)
        if SLFM.is_valid():
            SK1 = SLFM.cleaned_data['skill1']
            EXPRT1 = SLFM.cleaned_data['expert1']
            SK2 = SLFM.cleaned_data['skill2']
            EXPRT2 = SLFM.cleaned_data['expert2']
            SK3 = SLFM.cleaned_data['skill3']
            EXPRT3 = SLFM.cleaned_data['expert3']
            SK4 = SLFM.cleaned_data['skill4']
            EXPRT4 = SLFM.cleaned_data['expert4']
            SK5 = SLFM.cleaned_data['skill5']
            EXPRT5 = SLFM.cleaned_data['expert5']
            SK6 = SLFM.cleaned_data['skill6']
            EXPRT6 = SLFM.cleaned_data['expert6']
            SK7 = SLFM.cleaned_data['skill7']
            EXPRT7 = SLFM.cleaned_data['expert7']
            SK8 = SLFM.cleaned_data['skill8']
            EXPRT8 = SLFM.cleaned_data['expert8']
            LANG1 = SLFM.cleaned_data['lang1']
            STR1 = SLFM.cleaned_data['str1']
            LANG2 = SLFM.cleaned_data['lang2']
            STR2 = SLFM.cleaned_data['str2']
            LANG3 = SLFM.cleaned_data['lang3']
            STR3 = SLFM.cleaned_data['str3']
            icon1 = SLFM.cleaned_data['Icon1']
            icon2 = SLFM.cleaned_data['Icon2']
            icon3 = SLFM.cleaned_data['Icon3']
            reg = LangSkill(skill1=SK1, skill2=SK2, skill3=SK3, skill4=SK4, skill5=SK5, skill6=SK6, skill7=SK7,
                            skill8=SK8, lang1=LANG1, lang2=LANG2, lang3=LANG3, Icon1=icon1, Icon2=icon2, Icon3=icon3,
                            expert1=EXPRT1, expert2=EXPRT2, expert3=EXPRT3, expert4=EXPRT4, expert5=EXPRT5,
                            expert6=EXPRT6, expert7=EXPRT7, expert8=EXPRT8, str1=STR1, str2=STR2, str3=STR3)
            reg.save()
            SLFM = LangSkillForm()
    else:
        SLFM = LangSkillForm()
    SLdata = LangSkill.objects.all()
    return render(request, 'adminLanguageSkills.html', {'form': SLFM, 'SLdata': SLdata})


@login_required(login_url='/user_login')
def portfolios(request):
    if request.method == 'POST':
        PFFM = PortfoliosForm(request.POST, request.FILES)
        if PFFM.is_valid():
            LNK = PFFM.cleaned_data['link']
            THMBNL = PFFM.cleaned_data['thumbnail']
            reg = Portfolios(link=LNK, thumbnail=THMBNL)
            reg.save()
            PFFM = PortfoliosForm()
    else:
        PFFM = PortfoliosForm()
    PFdata = Portfolios.objects.all()
    return render(request, 'adminPortfolios.html', {'form': PFFM, 'PFdata': PFdata})


@login_required(login_url='/user_login')
def recommendation(request):
    if request.method == 'POST':
        RECFM = RecommendationsForm(request.POST, request.FILES)
        if RECFM.is_valid():
            PER = RECFM.cleaned_data['person']
            DESG = RECFM.cleaned_data['designation']
            DESC = RECFM.cleaned_data['description']
            reg = Recommendations(person=PER, designation=DESG, description=DESC)
            reg.save()
            RECFM = RecommendationsForm()
    else:
        RECFM = RecommendationsForm()
    RECdata = Recommendations.objects.all()
    return render(request, 'adminRecommendations.html', {'form': RECFM, 'RECdata': RECdata})


@login_required(login_url='/user_login')
def social_media(request):
    if request.method == 'POST':
        SMFM = SocialMediaForm(request.POST, request.FILES)
        if SMFM.is_valid():
            EM = SMFM.cleaned_data['email']
            SK = SMFM.cleaned_data['skype']
            PH = SMFM.cleaned_data['phone']
            GIT = SMFM.cleaned_data['github']
            LIK = SMFM.cleaned_data['linkedin']
            GP = SMFM.cleaned_data['google_plus']
            YTB = SMFM.cleaned_data['youtube']
            WEB = SMFM.cleaned_data['website']
            reg = SocialMedia(email=EM, skype=SK, phone=PH, github=GIT, linkedin=LIK, google_plus=GP, youtube=YTB,
                              website=WEB)
            reg.save()
            SMFM = SocialMediaForm()
    else:
        SMFM = SocialMediaForm()
    SMdata = SocialMedia.objects.all()
    return render(request, 'adminSocialmedia.html', {'form': SMFM, 'SMdata': SMdata})


@login_required(login_url='/user_login')
def adminblog(request):
    if request.method == 'POST':
        TIT = request.POST.get('title')
        HD = request.POST.get('heading')
        TGS = request.POST.get('tags')
        QT = request.POST.get('quote')
        QTBY = request.POST.get('quote_by')
        CRA = request.POST.get('created_at')
        DSC = request.POST.get('editor1')
        ICN = request.FILES['icon']
        reg = userBlog(title=TIT, heading=HD, tags=TGS, quote=QT, quote_by=QTBY, description=DSC, Icon=ICN,
                       created_at=CRA)
        reg.save()

    BLGdata = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLGdata, 10)
    pageNo = request.GET.get('page')
    BLGdataFINAL = paginator.get_page(pageNo)
    totalPages = BLGdataFINAL.paginator.num_pages
    context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
    return render(request, 'adminBlog.html', context)


def adminPIAIC(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        tags = request.POST.get('tags')
        instructions = request.POST.get('instructions')
        instructions_By = request.POST.get('instructions_By')
        description = request.POST.get('editor1')
        files = request.FILES.getlist('files')
        icons = request.FILES.getlist('icons')
        sv = PIAIC(title=title, heading=heading, tags=tags, instructions=instructions, instructions_By=instructions_By,
                   description=description)
        sv.save()
        latest_id = PIAIC.objects.latest('sNo').sNo

        for f in files:
            Attachments = PIAIC_Attachments(files=f, Attachment_ID_id=latest_id)
            Attachments.save()

        for f in icons:
            ICONS = PIAIC_ICONS(icons=f, Icon_ID_id=latest_id)
            ICONS.save()

        return redirect('/adminPIAIC')

    all_data = PIAIC.objects.all().order_by('-sNo')
    return render(request, 'adminPIAIC.html', {'all_data': all_data})


def PIAIC_Notifi(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        tags = request.POST.get('tags')
        instructions = request.POST.get('instructions')
        instructions_By = request.POST.get('instructions_By')
        description = request.POST.get('editor1')
        file = request.FILES.get('file')
        sv = PIAIC_Notifications(title=title, heading=heading, tags=tags, instructions=instructions, instructions_By=instructions_By,
                                 description=description, image=file)
        sv.save()
        return redirect('/adminPIAIC_Notifications')

    all_data = PIAIC_Notifications.objects.all().order_by('-sNo')
    return render(request, 'adminPIAIC_Notifications.html', {'all_data': all_data})


def user_comments(request):
    comment_data = blog_Review.objects.all()
    return render(request, 'comments.html', {'comment_data': comment_data})

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Delete Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
def Delete(request, id, type):
    if type == 'about':
        DELLABT = About.objects.get(id=id)
        DELLABT.delete()
        return redirect('/about')

    if type == 'experience':
        DELLEXP = Experience.objects.get(id=id)
        DELLEXP.delete()
        return redirect('/experience')

    if type == 'education':
        DELLEDU = Education.objects.get(id=id)
        DELLEDU.delete()
        return redirect('/education')

    if type == 'language_skills':
        DELLLNSK = LangSkill.objects.get(id=id)
        DELLLNSK.delete()
        return redirect('/languageskills')

    if type == 'portfolios':
        DELLPF = Portfolios.objects.get(id=id)
        DELLPF.delete()
        return redirect('/portfolios')

    if type == 'recommendation':
        DELLREC = Recommendations.objects.get(id=id)
        DELLREC.delete()
        return redirect('/recommendation')

    if type == 'socialMedia':
        DELLSM = SocialMedia.objects.get(id=id)
        DELLSM.delete()
        return redirect('/socialmedia')

    if type == 'Messages':
        DELLMSG = hello.objects.get(id=id)
        DELLMSG.delete()
        return redirect('/admin')

    if type == 'blog':
        DeleteRecord = userBlog.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminblog')

    if type == 'piaic_admin':
        DeleteRecord = PIAIC.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminPIAIC')

    if type == 'piaic_notification':
        DeleteRecord = PIAIC_Notifications.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminPIAIC_Notifications')

    if type == 'user_comment':
        DeleteRecord = blog_Review.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/user_comments')


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Update Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
def Update(request, id, type):
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

