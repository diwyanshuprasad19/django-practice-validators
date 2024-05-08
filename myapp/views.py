from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .request_validator import RequestValidator
from .exceptions import InvalidInputException
import json

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}

@csrf_exempt
def validate_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Assuming data is sent as JSON
            validator = RequestValidator(schema)  # Instantiate validator inside the view function
            validator.validate(data)
            return JsonResponse({'message': 'Data is valid'})
        except InvalidInputException as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
