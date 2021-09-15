from .models import Vendor;

def is_valid_cnpj(cnpj: str) -> bool:
    try:
        vendor = Vendor.objects.get(cnpj=cnpj);
    except Vendor.DoesNotExist: 
        return True;

    return False;



