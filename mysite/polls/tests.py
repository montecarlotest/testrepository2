from django.test import TestCase
from django.utils import timezone
from .models import  Question,Choice
import datetime
from django.core.urlresolvers import reverse
import pprint
# Create your tests here.

def create_question(question_text,days):
    """
    create a question with the given 'question_text' and given number of days
    offset to now (negative for question published in the poast and positive for
    question published in the futur
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return false for Question  whose
        pub_date is in the future
        :return false:
        """
        time=timezone.now()+datetime.timedelta(days=1)
        future_question=Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(),False )

class QuestionViewTest(TestCase):
    def test_index_view_with_no_question(self):
        """
        if no question exist,an appropriate message should be displayed
        :return:
        """
        response=self.client.get(reverse("polls:indexView"))
        pprint.pprint(response.__str__())
        print(response.content)
        print(response.context)
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])