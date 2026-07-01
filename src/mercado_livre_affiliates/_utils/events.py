from typing import AsyncGenerator, Any, Literal
from datetime import datetime, timedelta, timezone

from playwright.async_api import Page, Locator

from .._models import DealOfTheDayProduct, LightningDealProduct
from ..enums import OfferCategory

PRODUCTS_DEALS_BY_CATEGORIES: dict[str, set[str]] = {
    "https://www.mercadolivre.com.br/ofertas?category=MLB1747": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AND_PICKUP_TRUCK_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1771": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MOTORCYCLE_AND_ATV_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6005": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MARINE_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438364": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.HEAVY_DUTY_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2227": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.VEHICLE_TOOLS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB188063": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.AUTOMOTIVE_CLEANING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456111": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.LUBRICANTS_AND_FLUIDS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB8531": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.GPS_NAVIGATORS_FOR_VEHICLES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB260634": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.PERFORMANCE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456046": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MARINE_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB22693": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AND_PICKUP_TRUCK_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB419936": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.HEAVY_DUTY_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB243551": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MOTORCYCLE_AND_ATV_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2238": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.TIRES_AND_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB255788": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.WHEELS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2239": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.VEHICLE_SAFETY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3381": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AUDIO.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1776": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.TUNING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456826": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.BEEKEEPING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456820": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.STORAGE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456833": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.RENEWABLE_ENERGY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456927": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.WORK_TOOLS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB454448": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.RURAL_INFRASTRUCTURE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB442343": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_INPUTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271641": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.LIVESTOCK_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1514": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_MACHINERY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB442351": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_MACHINERY_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB457052": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.ANIMAL_PRODUCTION.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456795": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.CROP_PROTECTION.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278123": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.BEVERAGES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB410883": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.PREPARED_FOOD.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439739": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.FRESH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455505": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.KEFIR.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1423": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.GROCERY_STORE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB436789": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.ANTIQUES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB393901": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.FLAGS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1806": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.BANKNOTES_AND_COINS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2662": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.SCULPTURES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1369": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.ART_AND_CRAFTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270263": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.HABERDASHERY_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB44011": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.SCHOOL_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5360": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.NUTRITION_AND_BREASTFEEDING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420332": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.WALKERS_AND_RIDE_ON_TOYS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420334": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_BATH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1392": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_TOYS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB40563": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.PLAYPEN.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420293": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.PACIFIERS_AND_TEETHERS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420375": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_HYGIENE_AND_CARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420295": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.MATERNITY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420409": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_STROLL.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420361": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_ROOM.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1396": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_CLOTHES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420353": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_HEALTH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5358": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_SAFETY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455174": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264751": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIRDRESSING_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264787": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.BARBERSHOP.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB199407": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.SKINCARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1263": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_CARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5383": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_REMOVAL.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB431646": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PHARMACY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB198312": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PERSONAL_HYGIENE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB29884": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.MANICURE_AND_PEDICURE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1248": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.MAKEUP.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6284": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PERFUMES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278194": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.BEAUTY_TREATMENTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432991": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ANTI_STRESS_AND_INGENUITY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6911": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.OUTDOORS_AND_PLAYGROUND.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1132": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ARTS_AND_ACTIVITIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264337": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.DOLLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2961": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ELECTRONIC_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432818": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PRETEND_PLAY_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455425": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BUILDING_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433069": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BEACH_AND_POOL_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3655": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BABY_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433060": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PLAYHOUSES_AND_PLAY_TENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433047": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.HAND_PUPPETS_AND_MARIONETTES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432873": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.HOBBIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB11229": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.MUSICAL_INSTRUMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB437648": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PARLOR_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432988": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BOARD_AND_CARD_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB255050": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TOY_LAUNCHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270072": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TABLES_AND_CHAIRS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6905": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.MINI_VEHICLES_AND_BICYCLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1910": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1166": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PLUSH_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432871": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TOY_VEHICLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1831": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ALBUMS_AND_STICKERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1451": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.FASHION_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455528": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.OUTERWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB188064": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.BERMUDA_SHORTS_AND_SHORTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3112": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.BLOUSES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB23262": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.FOOTWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB188065": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.PANTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB107292": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.SHIRTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB31447": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.T_SHIRTS_AND_TANK_TOPS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271862": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.WORK_AND_SCHOOL_ATTIRE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271219": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.CLOTHING_SET_KITS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278018": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.LEGGINGS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB27250": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.OVERALLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1457": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.SUITCASES_AND_BAGS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270215": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.ACTIVEWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430391": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.BEACHWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB108786": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.INTIMATE_APPARE_AND_LINGERIE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5366": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.BABY_CLOTHES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB185489": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.SKIRTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB108831": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.SUITS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB108704": {
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.value(),
        OfferCategory.FOOTWEAR_CLOTHING_AND_BAGS.DRESSES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1613": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.RESTROOMS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438928": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.BEDS_MATTRESSES_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1618": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.KITCHEN.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264051": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.HOME_CARE_AND_LAUNDRY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1631": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.ORNAMENTS_AND_HOME_DECOR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1582": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.RESIDENTIAL_LIGHTING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1621": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.GARDEN_AND_OUTDOORS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB436380": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.HOME_FURNITURE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB436414": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.HOME_ORGANIZATION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB7069": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.HOME_SECURITY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB436246": {
        OfferCategory.HOME_FURNITURE_AND_DECOR.value(),
        OfferCategory.HOME_FURNITURE_AND_DECOR.HOME_TEXTILES_AND_DECOR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3813": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.MOBILE_PHONE_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1055": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.MOBILE_PHONE_AND_SMARTPHONES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB7462": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.CELL_PHONE_PARTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2908": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.TWO_WAY_RADIOS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1051": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.SMARTWATCHES_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB7502": {
        OfferCategory.CELL_PHONES_AND_TELEPHONES.value(),
        OfferCategory.CELL_PHONES_AND_TELEPHONES.VOIP.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438772": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.OPENINGS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455443": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.CONSTRUCTION_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB435273": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.PLUMBING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2467": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.ENERGY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB241354": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.PAINT_SHOP.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB403697": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.CONSTRUCTION_MATERIALS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB269773": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.BATHROOM_FURNITURE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB269958": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.KITCHEN_FURNITURE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1502": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.CONSTRUCTION_MACHINERY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB14548": {
        OfferCategory.CONSTRUCTION.value(),
        OfferCategory.CONSTRUCTION.FLOORING_AND_GROUT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1049": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.CAMERA_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB191839": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.CAMERAS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430403": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.DRONES_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6989": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.CAMCORDERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4062": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.OPTICAL_INSTRUMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438021": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.LENSES_AND_FILTERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB437831": {
        OfferCategory.CAMERAS_AND_ACCESSORIES.value(),
        OfferCategory.CAMERAS_AND_ACCESSORIES.ALBUMS_AND_PHOTO_FRAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB252358": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.AIR_AND_VENTILATION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB21171": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.WATER_COOLERS_AND_PURIFIERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439347": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.PERSONAL_CARE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1580": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.OVENS_AND_STOVES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438282": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.WASHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1899": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438284": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.SMALL_APPLIANCES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1576": {
        OfferCategory.HOME_APPLIANCES.value(),
        OfferCategory.HOME_APPLIANCES.REFRIGERATION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1007": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.TV_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4887": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.AUDIO_AND_VIDEO_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1001": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.DVD_AND_BLU_RAY_PLAYERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB10737": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.CABLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6999": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.ELECTRONIC_COMPONENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4914": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.REMOTE_CONTROLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264065": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.DRONES_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB133950": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.MEDIA_STREAMING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4900": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.BATTERIES_AND_CHARGERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2830": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.PROJECTORS_AND_SCREENS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1002": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.TELEVISIONS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3835": {
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.value(),
        OfferCategory.ELECTRONICS_AUDIO_AND_VIDEO.AUDIO.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2480": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.MARTIAL_ARTS_AND_BOXING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1309": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.BASKETBALL.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1362": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.CAMPING_HUNTING_AND_FISHING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1978": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.CANOES_KAYAKS_AND_INFLATABLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1292": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.CYCLING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB223498": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.HORSEBACK_RIDING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB421368": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SKIING_AND_SNOWBOARDING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1338": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.FITNESS_AND_WEIGHT_TRAINING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1286": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SOCCER.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438767": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.HANDBALL.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438999": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.PARLOR_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1279": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.DIVE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1339": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.ACTIVEWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB123103": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SPORTS_INSTRUCTORS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1278": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SWIMMING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB410723": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.KICK_SCOOTERS_AND_MOTOR_SCOOTERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1293": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.ROLLER_SKATING_AND_SKATEBOARDING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1357": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.RAPPELING_MOUNTAINEERING_AND_ROCK_CLIMBING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438178": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SUPPLEMENTS_AND_SHAKERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB440904": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.SHOOTING_SPORTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3900": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.TENNIS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1322": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.TENNIS_PADEL_AND_SQUASH.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB422153": {
        OfferCategory.SPORTS_AND_FITNESS.value(),
        OfferCategory.SPORTS_AND_FITNESS.VOLLEYBALL.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2528": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.TOOL_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB189210": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.BOXES_AND_ORGANIZERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2526": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.POWER_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439064": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.INDUSTRIAL_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2527": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.HAND_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB437789": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.PNEUMATIC_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB269932": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.GARDEN_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5550": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.MEASUREMENTS_AND_INSTRUMENTATION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5236": {
        OfferCategory.TOOLS.value(),
        OfferCategory.TOOLS.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB256810": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_SUPPLIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB50656": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_DECORATION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB256841": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_DISPOSABLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB457417": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438497": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.FOAM_STREAMERS_AND_CONFETTI.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455857": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.COSTUMES_AND_COSPLAY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB40189": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_FAVORS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB457521": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.PARTY_FAVORS_FOR_PARTIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB46237": {
        OfferCategory.PARTIES_AND_PARTY_FAVORS.value(),
        OfferCategory.PARTIES_AND_PARTY_FAVORS.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438578": {
        OfferCategory.GAMES.value(),
        OfferCategory.GAMES.CONSOLE_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439527": {
        OfferCategory.GAMES.value(),
        OfferCategory.GAMES.PC_GAMING_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB11172": {
        OfferCategory.GAMES.value(),
        OfferCategory.GAMES.CONSOLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438579": {
        OfferCategory.GAMES.value(),
        OfferCategory.GAMES.CONSOLE_PARTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB186456": {
        OfferCategory.GAMES.value(),
        OfferCategory.GAMES.VIDEO_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438906": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.ARCHITECTURE_AND_DESIGN.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270864": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.PACKAGING_AND_LOGISTICS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB454798": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.MEDICAL_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5452": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.COMMERCIAL_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2102": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.OFFICE_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB454785": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.INDUSTRIAL_TOOLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB268412": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.GASTRONOMY_AND_HOSPITALITY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5446": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.PRINTING_SERVICES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1893": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439267": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.ADVERTISING_AND_PROMOTION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270252": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.WORKPLACE_SAFETY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5454": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.TEXTILES_AND_FOOTWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439268": {
        OfferCategory.INDUSTRY_AND_COMMERCE.value(),
        OfferCategory.INDUSTRY_AND_COMMERCE.UNIFORMS_AND_WORKWEAR.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB447778": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PC_GAMING_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430598": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.STORAGE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430918": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.USB_CABLES_AND_HUBS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1712": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PC_COMPONENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1700": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.CONNECTIVITY_AND_NETWORKING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1718": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.VOLTAGE_STABILIZERS_AND_UPS_UNITS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5875": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PRINT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271908": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.READERS_AND_SCANNERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB99944": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PC_CLEANING.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB14370": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.MONITORS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430637": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.DESKTOP_PC.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1651": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PALM_DEVICES_AND_HANDLEHELDS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB454379": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.PC_PERIPHERALS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB430687": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.LAPTOPS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1657": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.MONITORS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1723": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.SOFTWARE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB91757": {
        OfferCategory.COMPUTING.value(),
        OfferCategory.COMPUTING.TABLETS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3004": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.DRUMS_AND_PERCUSSION.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4472": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.SPEAKERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4474": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.DJ_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB434917": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.RECORDING_STUDIO.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278055": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.STRING_INSTRUMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278056": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.WIND_INSTRUMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4479": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.METRONOMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB434816": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.MICROPHONES_AND_AMPLIFIERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438490": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.SHEET_MUSIC_AND_LYRICS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432934": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.PEDALS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3022": {
        OfferCategory.MUSICAL_INSTRUMENTS.value(),
        OfferCategory.MUSICAL_INSTRUMENTS.PIANOS_AND_KEYBOARDS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB118024": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.WATCH_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB404419": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.JEWELRY_ITEMS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1431": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.FINE_JEWELRY_AND_COSTUME_JEWELRY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3938": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1441": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.PRECIOUS_AND_SEMI_PRECIOUS_STONES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5122": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.PIERCINGS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB40282": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.JEWELRY_BOX.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB118017": {
        OfferCategory.JEWELRY_AND_WATCHES.value(),
        OfferCategory.JEWELRY_AND_WATCHES.WATCHES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB437616": {
        OfferCategory.BOOKS_MAGAZINES_AND_COMICS.value(),
        OfferCategory.BOOKS_MAGAZINES_AND_COMICS.PHYSICAL_BOOKS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1227": {
        OfferCategory.BOOKS_MAGAZINES_AND_COMICS.value(),
        OfferCategory.BOOKS_MAGAZINES_AND_COMICS.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270192": {
        OfferCategory.MORE_CATEGORIES.value(),
        OfferCategory.MORE_CATEGORIES.TATTOO_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1740": {
        OfferCategory.MORE_CATEGORIES.value(),
        OfferCategory.MORE_CATEGORIES.ESOTERICISM_AND_OCCULTISM.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1100": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.BIRDS_AND_ACCESSORIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1117": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.HORSES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1072": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.DOGS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1081": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.CATS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB85855": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.PET_LEASHES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1091": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.FISH.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB458045": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.PET_FOOD_CONTAINER.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1105": {
        OfferCategory.PET_SHOP.value(),
        OfferCategory.PET_SHOP.RODENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264192": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.HEALTHCARE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB277969": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.MEDICAL_EQUIPMENT.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB10217": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.MASSAGE.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264180": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.MOBILITY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264200": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.ORTHOPEDICS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264678": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264201": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.DIETARY_SUPPLEMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438401": {
        OfferCategory.HEALTH.value(),
        OfferCategory.HEALTH.ALTERNATIVE_THERAPIES.value()
    }
}


def add_promotion_type_to_url(
    url: str, promotion_type: Literal["deal_of_the_day", "lightning"]
) -> str:
    if "?" in url:
        return url + f"&promotion_type={promotion_type}"
    return url + f"?promotion_type={promotion_type}"


async def extract_price(locator: Locator) -> dict[str, int]:
    if await locator.count() > 0:
        price: dict[str, int] = {}
        locator_attribute = await locator.get_attribute("aria-label")
        if locator_attribute is None:
            raise
        price["reais"] = int(
            locator_attribute[
                locator_attribute.index(": ")
                + len(": ") : locator_attribute.index(" reais") :
            ]
        )
        if locator_attribute.count("centavos") == 1:
            price["cents"] = int(
                locator_attribute[
                    locator_attribute.index("com ")
                    + len("com ") : locator_attribute.index("centavos") :
                ]
            )
        else:
            price["cents"] = 0
        return price
    raise RuntimeError("Price not found")


async def extract_title(locator: Locator) -> str:
    if await locator.count() > 0:
        return await locator.inner_text()
    raise RuntimeError("Title not found")


async def extract_rating(locator: Locator) -> float:
    if await locator.count() > 0:
        return float(await locator.inner_text())
    raise RuntimeError("Rating not found")


async def extract_url(locator: Locator) -> str:
    if await locator.count() > 0:
        url = await locator.get_attribute("href")
        if url is not None:
            return url
    raise RuntimeError("Product URL not found")


async def extract_image_url(locator: Locator) -> str:
    if await locator.count() > 0:
        url = await locator.first.get_attribute("src")
        if url is not None:
            return url
    raise RuntimeError("Image URL not found")


async def extract_total_reviews(locator: Locator) -> int:
    if await locator.count() > 0:
        return int((await locator.inner_text()).strip("()"))
    raise RuntimeError("Total reviews not found")


async def generate_countdown_timestamp(locator: Locator) -> datetime:
    if await locator.count() > 0:
        countdown_parts = ((await locator.inner_text()).replace("\n", "")).split(":")
        hours = (int(countdown_parts[0][0]) * 10) + int(countdown_parts[0][1])
        minutes = (int(countdown_parts[1][0]) * 10) + int(countdown_parts[1][1])
        seconds = (int(countdown_parts[2][0]) * 10) + int(countdown_parts[2][1])
        return datetime.now(tz=timezone.utc) + timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )
    raise RuntimeError("Countdown not found")


async def web_scraping_deals_of_the_day_products(
    page: Page,
) -> AsyncGenerator[DealOfTheDayProduct, None]:
    for url, categories in PRODUCTS_DEALS_BY_CATEGORIES.items():
        url = add_promotion_type_to_url(url=url, promotion_type="deal_of_the_day")
        await page.goto(url=url)
        has_next_page = True
        while has_next_page:
            products_locators = await page.locator(".poly-card").all()
            if len(products_locators) == 0:
                has_next_page = False
                continue
            for product_locator in products_locators:
                try:
                    product: dict[str, Any] = {"categories": categories}
                    locator = product_locator.locator(".poly-component__title")
                    product["title"] = await extract_title(locator=locator)
                    product["url"] = await extract_url(locator=locator)
                    locator = product_locator.locator("img")
                    product["image_url"] = await extract_image_url(locator=locator)
                    locator = product_locator.locator(".poly-reviews__rating")
                    product["rating"] = await extract_rating(locator=locator)
                    locator = product_locator.locator(".poly-reviews__total")
                    product["total_reviews"] = await extract_total_reviews(
                        locator=locator
                    )
                    locator = product_locator.locator(".andes-money-amount--previous")
                    product["old_price"] = await extract_price(locator=locator)
                    locator = product_locator.locator(
                        ".poly-price__current .andes-money-amount"
                    )
                    product["current_price"] = await extract_price(locator=locator)
                    yield DealOfTheDayProduct(**product)
                except Exception:
                    continue
            next_button = page.locator(
                ".andes-pagination__button--next a, li.andes-pagination__button--next a"
            )
            if await next_button.count() > 0 and await next_button.is_visible():
                current_url = page.url
                await next_button.click()
                if page.url == current_url:
                    has_next_page = False
            else:
                has_next_page = False


async def web_scraping_lightning_deals_products(
    page: Page,
) -> AsyncGenerator[LightningDealProduct, None]:
    for url, categories in PRODUCTS_DEALS_BY_CATEGORIES.items():
        url = add_promotion_type_to_url(url=url, promotion_type="lightning")
        await page.goto(url=url)
        has_next_page = True
        while has_next_page:
            products_locators = await page.locator(".poly-card").all()
            if len(products_locators) == 0:
                has_next_page = False
                continue
            for product_locator in products_locators:
                try:
                    product: dict[str, Any] = {"categories": categories}
                    locator = product_locator.locator(".poly-component__countdown")
                    product["expires_in"] = await generate_countdown_timestamp(
                        locator=locator
                    )
                    locator = product_locator.locator(".poly-component__title")
                    product["title"] = await extract_title(locator=locator)
                    product["url"] = await extract_url(locator=locator)
                    locator = product_locator.locator("img")
                    product["image_url"] = await extract_image_url(locator=locator)
                    locator = product_locator.locator(".poly-reviews__rating")
                    product["rating"] = await extract_rating(locator=locator)
                    locator = product_locator.locator(".poly-reviews__total")
                    product["total_reviews"] = await extract_total_reviews(
                        locator=locator
                    )
                    locator = product_locator.locator(".andes-money-amount--previous")
                    product["old_price"] = await extract_price(locator=locator)
                    locator = product_locator.locator(
                        ".poly-price__current .andes-money-amount"
                    )
                    product["current_price"] = await extract_price(locator=locator)
                    yield LightningDealProduct(**product)
                except Exception:
                    continue
            next_button = page.locator(
                ".andes-pagination__button--next a, li.andes-pagination__button--next a"
            )
            if await next_button.count() > 0 and await next_button.is_visible():
                current_url = page.url
                await next_button.click()
                if page.url == current_url:
                    has_next_page = False
            else:
                has_next_page = False
