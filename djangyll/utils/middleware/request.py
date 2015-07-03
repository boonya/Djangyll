class ParseAndSetRawRequestDataIntoPost(object):

    @staticmethod
    def process_request(request):
        """
        Manipulates the request object before passing it to view functions.

        :param request:
        :return:
        """
        try:
            # @TODO: Fix this shit
            request.POST = request.body
        except ValueError:
            pass
