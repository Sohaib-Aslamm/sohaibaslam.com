from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia,\
hello, userBlog, blog_Review, PIAIC, PIAIC_Notifications, seoTags, MainPage


from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def Delete(request, id, type):
    if type == 'main_page':
        DELLMNP = MainPage.objects.get(id=id)
        DELLMNP.delete()
        return redirect('/main_page')

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

    if type == 'seoTags':
        DeleteRecord = seoTags.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/seotags')
