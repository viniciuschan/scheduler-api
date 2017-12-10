from rest_framework.test import APITransactionTestCase

from app.models import Procedure


class ProcedureTestCase(APITransactionTestCase):
    """ Test cases for the patient API """

    def setUp(self):

        Procedure.objects.create(
            id=1,
            description="Consulta",
            cost="100.00"
        )

        Procedure.objects.create(
            id=2,
            description="Exame",
            cost="100
        )