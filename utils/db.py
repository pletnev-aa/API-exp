from callback.models import Billing, Company, Customer, Service


def save_data(data):
    customer = add_customer(data[0])
    company = add_company(data[1])
    services = add_service(data[5:])
    if not Billing.objects.filter(customer=customer, company=company, account=data[2]).exists():
        invoice = Billing.objects.create(
            customer=customer,
            company=company,
            account=data[2],
            price=data[3],
            date=data[4]
        )
        for service in services:
            invoice.services.add(service)
        invoice.save()


def add_customer(customer):
    if not Customer.objects.filter(name=customer).exists():
        Customer.objects.create(name=customer)
    return Customer.objects.get(name=customer)


def add_company(company):
    if not Company.objects.filter(name=company).exists():
        Company.objects.create(name=company)
    return Company.objects.get(name=company)


def add_service(values):
    services = []
    for service in values:
        if not Service.objects.filter(name=service).exists():
            Service.objects.create(name=service)
        services.append(
            Service.objects.get(name=service)
        )
    return services
            