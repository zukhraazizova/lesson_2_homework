from adress import Adress
from mailing import Mailing


from_address = Adress(36700,"mah","lenina","3","27")
to_address = Adress(36567,"mos","push","6","77")
mailing = Mailing (from_address , to_address, "100rb","45")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей."
)
