from flask import Response, json


def success(data={}, content_type='application/json'):
    return Response(
        response=json.dumps({'success': True, 'data': data}),
        content_type=content_type,
        status=200
    )


def fail(data={}, status=400, content_type='application/json'):
    return Response(
        response=json.dumps({'success': False, 'data': data}),
        content_type=content_type,
        status=status
    )
