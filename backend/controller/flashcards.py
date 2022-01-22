from fastapi import APIRouter, status, Request, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import backend.repository.flashcards as repository
import backend.entity.flashcards as entity
import backend.controller.flashcards_dto as dto
router = APIRouter()
security = HTTPBearer()


@router.post('/flashcards/category', status_code=status.HTTP_201_CREATED)
def add_category(request: Request,
                 category_dto: dto.Category,
                 credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    payload = request.app.state.authenticate.decode_token(token)
    if payload['role'] == 3:
        raise HTTPException(status_code=403, detail='unauthorized')
    category_id = repository.Category(
        request.app.state.database).category_id(category_dto.name)
    if category_id is not None:
        raise HTTPException(status_code=409, detail='Category exist')
    repo = repository.Category(request.app.state.database)
    category_entity = entity.Category(category_dto.name)
    return repo.insert(category_entity)


@router.get('/flashcards/category')
def get_all_categories(request: Request):
    repo = repository.Category(request.app.state.database)
    return repo.select_all()


@router.post('/flashcards/category/subcategory', status_code=status.HTTP_201_CREATED)
def get_all_subcategories_from_category(request: Request,
                                        subcategory_dto: dto.Subcategory,
                                        credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    payload = request.app.state.authenticate.decode_token(token)
    if payload['role'] == 3:
        raise HTTPException(status_code=403, detail='unauthorized')
    repo = repository.Subcategory(request.app.state.database)
    category_id = repository.Category(
        request.app.state.database).category_id(subcategory_dto.category_name)
    category_id = category_id[0]
    if category_id is None:
        raise HTTPException(status_code=404, detail='Category not found')
    if repo.subcategory_id(category_id, subcategory_dto.name) is not None:
        raise HTTPException(status_code=409, detail='Subategory exist')
    category_entity = entity.Subcategory(subcategory_dto.name,
                                         category_id)
    return repo.insert(category_entity)


@router.get('/flashcards/{category_name}')
def get_all_subcategories_from_category(request: Request, category_name):
    repo = repository.Subcategory(request.app.state.database)
    return repo.select_all_subcategories_from_category(category_name)


@router.post('/flashcards', status_code=status.HTTP_201_CREATED)
def add_flashcard(request: Request,
                  set_card: dto.SetCard,
                  credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    payload = request.app.state.authenticate.decode_token(token)
    repo = repository.Category(request.app.state.database)
    category_id = repo.category_id(set_card.category_name)
    category_id = category_id[0]
    repo = repository.Subcategory(request.app.state.database)
    subcategory_id = repo.subcategory_id(
        category_id, set_card.subcategory_name)
    subcategory_id = subcategory_id[0]
    repo = repository.SetCards(request.app.state.database)

    set_card_entity = entity.SetCards(
        set_card.name, int(subcategory_id), int(payload['sub']))

    print(set_card_entity.subcategory_id)
    print(set_card_entity.user_id)

    set_card_id = repo.insert(set_card_entity)
    # for card in set_card.cards:
    #         question_entity = entity.Question(card.question.content)
    #         answer_entity

    #     set_card_entity
    #     print(card.question.content)
