# ТЗ: Customer Churn Prediction Service (ML + Cloud Deployment)

## Мета проєкту
Закрити дві найчастіші прогалини в резюме, що зринали при відгуках: **реальний ML** (класифікація/прогнозування, не LLM-wrapper) і **Cloud deployment** (Azure/AWS/GCP). Побудувати на існуючому стеку (Python, FastAPI, Docker), не вчити все з нуля.

## Резюме-формулювання (для майбутнього)
> Built and deployed a customer churn prediction service — trained a classification model on 7,000+ customer records, exposed it via a FastAPI endpoint, containerized with Docker, and deployed to Azure App Service with a CI/CD pipeline via GitHub Actions.

---

## Етап 1 — Дані та дослідницький аналіз (EDA)

**Датасет:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) — ~7,000 рядків, готовий, чистий, стандартний бенчмарк для junior-рівня.

**Завдання:**
- [ ] Завантажити датасет, покласти в `data/raw/`
- [ ] Notebook `01_eda.ipynb`: розподіл цільової змінної (Churn: Yes/No), пропущені значення, кореляції числових ознак
- [ ] Візуалізації (Matplotlib/Seaborn): churn rate по контракту, по tenure, по monthly charges
- [ ] Зафіксувати 3-5 інсайтів текстом у notebook (це показує аналітичне мислення, не тільки код)

**Definition of Done:** notebook з графіками + короткий текстовий висновок нагорі файлу.

---

## Етап 2 — Препроцесинг та Feature Engineering

**Завдання:**
- [ ] Обробка категоріальних змінних (One-Hot Encoding / Label Encoding)
- [ ] Обробка пропущених значень (`TotalCharges` у цьому датасеті має приховані пропуски як пробіли — класична pitfall, знайти і обробити)
- [ ] Train/test split (стратифікований, бо цільова змінна незбалансована)
- [ ] Масштабування числових ознак (StandardScaler) де потрібно
- [ ] Зберегти pipeline препроцесингу через `sklearn.Pipeline` (не робити вручну кожен раз — це важливо для продакшн-коду)

**Definition of Done:** `src/preprocessing.py` з функцією/класом, що повертає готовий до навчання X_train/X_test.

---

## Етап 3 — Модель

**Завдання:**
- [ ] Базова модель: Logistic Regression (baseline)
- [ ] Основна модель: Random Forest або XGBoost
- [ ] Метрики: **не тільки accuracy** — Precision, Recall, F1, ROC-AUC (датасет незбалансований, accuracy оманлива — показати, що ти це розумієш, важливо для співбесіди)
- [ ] Confusion matrix — візуалізація
- [ ] Feature importance — які фактори найбільше впливають на відтік (бізнес-цінність, не тільки метрики)
- [ ] Зберегти модель через `joblib`/`pickle` у `models/churn_model.pkl`

**Definition of Done:** notebook `02_model_training.ipynb` + збережена модель + таблиця метрик у README.

---

## Етап 4 — API (FastAPI)

**Завдання:**
- [ ] `POST /predict` — приймає JSON з ознаками клієнта, повертає ймовірність відтоку + клас (Yes/No)
- [ ] `GET /health` — health-check ендпоінт (стандарт для деплою, показує розуміння production-readiness)
- [ ] Pydantic-модель для валідації вхідних даних
- [ ] Завантаження моделі один раз при старті додатку (не на кожен запит)
- [ ] Базова обробка помилок (невалідний вхід → зрозуміла 422-відповідь, не 500)

**Definition of Done:** `uvicorn main:app` працює локально, `/docs` (Swagger) показує робочий ендпоінт.

---

## Етап 5 — Docker

**Завдання:**
- [ ] `Dockerfile` (multi-stage build — showcase хорошої практики, менший образ)
- [ ] `docker-compose.yml` (навіть якщо сервіс один — стандарт для читабельності)
- [ ] Перевірити, що образ збирається і запускається локально (`docker build` + `docker run`)

**Definition of Done:** `docker run -p 8000:8000 churn-api` → `/health` відповідає 200.

---

## Етап 6 — Деплой на Azure

**Завдання:**
- [ ] Створити безкоштовний Azure-акаунт (Student-tier якщо є доступ через STU — часто дають $100 кредиту)
- [ ] Azure App Service (Web App for Containers) — задеплоїти Docker-образ напряму
- [ ] Альтернатива, якщо Azure виявиться складним з першого разу: Render.com або Railway (безкоштовні, простіші, теж "cloud deployment" по суті) — не soromitis, головне мати working link
- [ ] Перевірити, що `/predict` відповідає на live-URL

**Definition of Done:** робоче публічне посилання на API (додати в README і в резюме).

---

## Етап 7 — CI/CD (bonus, якщо є час)

**Завдання:**
- [ ] `.github/workflows/ci.yml` — GitHub Actions: при кожному push у main — запускати pytest (хоча б 2-3 базові тести на API-ендпоінт)
- [ ] Опційно: авто-деплой на Azure при пуші в main

**Definition of Done:** зелена галочка в GitHub Actions на останньому коміті.

---

## Етап 8 — README (найважливіше для рекрутера)

**Структура README.md:**
1. Одне речення — що робить проєкт
2. Business problem (навіщо компаніям прогнозувати churn — 2-3 речення)
3. Architecture diagram (можна просто текстова схема: Data → Model → FastAPI → Docker → Azure)
4. Key results (метрики моделі, конкретні цифри)
5. Tech stack (список)
6. Live demo link
7. Як запустити локально (для тих, хто дивиться репо)

---

## Тайм-менеджмент (орієнтовно)

| Етап | Час |
|---|---|
| EDA + Preprocessing | 3-4 год |
| Модель + метрики | 3-4 год |
| FastAPI | 2-3 год |
| Docker | 1-2 год |
| Azure deploy | 2-4 год (перший раз завжди довше через налаштування акаунту) |
| CI/CD (bonus) | 1-2 год |
| README | 1 год |
| **Разом** | **~15-20 год** |

## Що НЕ робити (щоб не роздувати scope)
- Не намагатись зробити state-of-the-art модель — junior-рівню достатньо ROC-AUC ~0.80-0.85 на цьому датасеті, головне показати процес і розуміння метрик
- Не робити фронтенд — API + Swagger docs достатньо
- Не використовувати Kubernetes чи складний оркестратор — це overkill, App Service вистачить
