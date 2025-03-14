import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, CalIn, CalOut  # Import your models

@csrf_exempt  # Remove CSRF for testing (not recommended in production)
def submit_calIn(request):
    """ Handle both JSON and form data """
    if request.method == "POST":
        try:
            # Handle JSON and form-data requests
            if request.content_type == "application/json":
                data = json.loads(request.body)
            else:
                data = request.POST.dict()  # Convert QueryDict to dict

            # Extract values
            this_token = data.get("token")
            this_text = data.get("text", "").strip()
            this_amount = data.get("amount")

            # Validate token (Check if user exists)
            try:
                this_user = User.objects.get(token__token=this_token)
            except User.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Invalid token, user not found"}, status=400)

            # Validate `text`
            if not this_text:
                return JsonResponse({"status": "error", "message": "Invalid text, cannot be empty"}, status=400)

            # Validate `amount` (should be a number)
            try:
                this_amount = float(this_amount)
                if this_amount <= 0:
                    return JsonResponse({"status": "error", "message": "Invalid amount, must be positive"}, status=400)
            except (TypeError, ValueError):
                return JsonResponse({"status": "error", "message": "Invalid amount, must be a number"}, status=400)

            # Handle optional date field (ensure the correct format for date if passed as a string)
            this_date = data.get("date", datetime.now())  # Use provided date or default to now
            if isinstance(this_date, str):  # If date is a string, parse it
                try:
                    this_date = datetime.fromisoformat(this_date)
                except ValueError:
                    return JsonResponse({"status": "error", "message": "Invalid date format"}, status=400)

            # Save data to `CalIn` model
            CalIn.objects.create(user=this_user, text=this_text, amount=this_amount, date=this_date)

            return JsonResponse({
                "status": "ok",
                "message": "Data received successfully"
            }, json_dumps_params={'indent': 2})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST requests allowed"}, status=400)


@csrf_exempt  # Remove CSRF for testing (not recommended in production)
def submit_calOut(request):
    """ Handle both JSON and form data """
    if request.method == "POST":
        try:
            # Handle JSON and form-data requests
            if request.content_type == "application/json":
                data = json.loads(request.body)
            else:
                data = request.POST.dict()  # Convert QueryDict to dict

            # Extract values
            this_token = data.get("token")
            this_text = data.get("text", "").strip()
            this_amount = data.get("amount")

            # Validate token (Check if user exists)
            try:
                this_user = User.objects.get(token__token=this_token)
            except User.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Invalid token, user not found"}, status=400)

            # Validate `text`
            if not this_text:
                return JsonResponse({"status": "error", "message": "Invalid text, cannot be empty"}, status=400)

            # Validate `amount` (should be a number)
            try:
                this_amount = float(this_amount)
                if this_amount <= 0:
                    return JsonResponse({"status": "error", "message": "Invalid amount, must be positive"}, status=400)
            except (TypeError, ValueError):
                return JsonResponse({"status": "error", "message": "Invalid amount, must be a number"}, status=400)

            # Handle optional date field (ensure the correct format for date if passed as a string)
            this_date = data.get("date", datetime.now())  # Use provided date or default to now
            if isinstance(this_date, str):  # If date is a string, parse it
                try:
                    this_date = datetime.fromisoformat(this_date)
                except ValueError:
                    return JsonResponse({"status": "error", "message": "Invalid date format"}, status=400)

            # Save data to `CalOut` model
            CalOut.objects.create(user=this_user, text=this_text, amount=this_amount, date=this_date)

            return JsonResponse({
                "status": "ok",
                "message": "Data received successfully"
            }, json_dumps_params={'indent': 2})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST requests allowed"}, status=400)
