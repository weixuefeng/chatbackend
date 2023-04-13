import logging

def access_required(func):
    """ Sign verification.
    :param func:
    :return: response
    """
    def _decorator(request, *args, **kwargs):
        # clean session cache
        # check user from access_token
        request.session['current_user'] = None
        request.session['current_user_id'] = None

        # try:
        #     # content_type = request.META.get('CONTENT_TYPE') or request.META.get['HTTP_CONTENT_TYPE']
        #     # if not request.POST and content_type == 'application/json':
        #     #     data = json.loads(request.body.decode('utf-8'))
        #     #     if data:
        #     #         request.POST = data
        #             # detect language
        #     language = language_utils.detect_language(request)
        #     translation.activate(language)
        #     request.LANGUAGE_CODE = translation.get_language()
        # except:
        #     pass

        # if settings.ENV_DEV == True and request.path != '/api/v1/sign/test/':
        #     response = func(request, *args, **kwargs)
        #     return response

        # sign = request.POST.get('sign')
        # app_key = request.POST.get('app_key')
        # if app_key in APP_KEY_TO_SECRET:
        #     logger.debug('app_key verification passed')
        #     # Verify timestamp.
        #     timestamp = request.POST.get('timestamp')
        #     if timestamp:
        #         now_time = time.time()
        #         interval_time = now_time - float(timestamp)
        #         if interval_time > 300:
        #             logger.error('The timestamp verify failed, interval time more than 300s.')
        #             return http.JsonErrorResponse(
        #                 error_code=codes.ErrorCode.TIMESTAMP_VERIFY_FAILED.value,
        #                 error_message='The timestamp verify failed, interval time more than 300s.')
        #     else:
        #         logger.error('The timestamp is empty.')
        #         return http.JsonErrorResponse(
        #             error_code=codes.ErrorCode.TIMESTAMP_IS_EMPTY.value,
        #             error_message='The timestamp is empty.')

        #     # Verify sign.
        #     secret = APP_KEY_TO_SECRET[app_key]
        #     signed_string = security.sign_hmac(request.POST, secret=secret)
        #     logger.debug('Received sign:%s' % sign)
        #     logger.debug('The sign calculated by the server:%s' % signed_string)
        #     if sign == signed_string:
        #         if STATUS_INFO.get('status') == codes.SystemServiceStatus.MAINTAIN.value:
        #             return http.JsonErrorResponse(codes.ErrorCode.MAINTAIN.value, error_message=(STATUS_INFO.get('msg')),
        #                                           data={'m_time': STATUS_INFO.get('m_time')})
        #         response = func(request, *args, **kwargs)
        #         logger.debug('send response is %s.' % response.content)
        #         return response
        #     else:
        #         logger.error("Sign value verification failed !")
        #         return http.JsonErrorResponse(error_message=_('Sign value verification failed !'))
        # else:
        #     logger.error('Failed to get app key.')
            # return http.JsonErrorResponse(error_message='Failed to get app key.')
    return _decorator
