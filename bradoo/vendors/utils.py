from .models import Vendor;
import re;

def is_valid_cnpj(cnpj: str) -> bool:

    # First check if given CNPJ is already taken 
    try:
        vendor = Vendor.objects.get(cnpj=cnpj);
    except Vendor.DoesNotExist: 
        # If it is not taken, check the format
        return is_valid_cnpj_format(cnpj);

    return False;

def is_valid_cnpj_format(cnpj: str) -> bool:

    cnpj.strip(" ");        # Remove whitespaces

    cnpj_re = re.compile(r"(\d{2})(\.)?(\d{3})(\.)?\d{3}(\/)?(0001)(-)?(\d{2})")
 
    mo = cnpj_re.search(cnpj);

    return mo is not None;

def get_vendor(body) -> Vendor:
    pk =   body.get("id");
    name = body.get("name");
    cnpj = body.get("CNPJ");

    if (pk is not None):
        try:
            vendor = Vendor.objects.get(pk=pk);
        except Vendor.DoesNotExist:
            return None;
        return vendor;
    
    if (cnpj is not None):
        try: 
            vendor = Vendor.objects.get(cnpj=cnpj);
        except Vendor.DoesNotExist:
            return None;

        return vendor;
        
    if (name is not None):
        try: 
            vendor = Vendor.objects.get(name=name);
        except Vendor.DoesNotExit or Vendor.IntegrityError:
            return None;
        return vendor;

def wrong_request(expected: str, given: str):
    return {"error": f"ERROR: {expected} request is required, got {given}."}
    


