
<canvas>
<line number="1" id="idx1"># 🚀 CoreHub</line>
<line number="2" id="idx2"></line>
<line number="3" id="idx3">CoreHub is a robust backend system built with **Django**, specialized in secure **OTP-based authentication** and modular architecture.</line>
<line number="4" id="idx4"></line>
<line number="5" id="idx5">## ✨ Features</line>
<line number="6" id="idx6">- 🔐 Secure OTP Auth</line>
<line number="7" id="idx7">- ⚡ Redis Caching</line>
<line number="8" id="idx8">- ⚙️ Celery Background Tasks</line>
<line number="9" id="idx9">- 🏗️ Modular Architecture</line>
<line number="10" id="idx10">- 📡 RESTful API (DRF)</line>
<line number="11" id="idx11"></line>
<line number="12" id="idx12">## 1. Environment Variables</line>
<line number="13" id="idx13">Before running the project, you must configure your environment variables. Create a `.env` file in the root directory and use the following template:</line>
<line number="14" id="idx14"></line>
<line number="15" id="idx15">
```env</line>
<line number="16" id="idx16">SECRET_KEY=your_secret_key_here</line>
<line number="17" id="idx17">DEBUG=True</line>
<line number="18" id="idx18">ALLOWED_HOSTS=localhost,127.0.0.1</line>
<line number="19" id="idx19"></line>
<line number="20" id="idx20"># Database</line>
<line number="21" id="idx21">DATABASE_URL=postgres://user:password@localhost:5432/dbname</line>
<line number="22" id="idx22"></line>
<line number="23" id="idx23"># Redis & Celery</line>
<line number="24" id="idx24">REDIS_URL=redis://localhost:6379/0</line>
<line number="25" id="idx25">CELERY_BROKER_URL=redis://localhost:6379/0</line>
<line number="26" id="idx26">CELERY_RESULT_BACKEND=redis://localhost:6379/1</line>
<line number="27" id="idx27"></line>
<line number="28" id="idx28"># SMS Services</line>
<line number="29" id="idx29">SMS_API_KEY=your_sms_api_key_here</line>
<line number="30" id="idx30">
```</line>
<line number="31" id="idx31"></line>
<line number="32" id="idx32">## 2. Installation & Setup</line>
<line number="33" id="idx33">### Clone & Enter</line>
<line number="34" id="idx34">
```bash</line>
<line number="35" id="idx35">git clone https://github.com/HOsouli/CoreHub.git</line>
<line number="36" id="idx36">cd CoreHub</line>
<line number="37" id="idx37">
```</line>
<line number="38" id="idx38"></line>
<line number="39" id="idx39">### Environment Setup</line>
<line number="40" id="idx40">**Windows:**</line>
<line number="41" id="idx41">
```bash</line>
<line number="42" id="idx42">python -m venv .venv</line>
<line number="43" id="idx43">.venv\Scripts\activate</line>
<line number="44" id="idx44">
```</line>
<line number="45" id="idx45">**macOS/Linux:**</line>
<line number="46" id="idx46">
```bash</line>
<line number="47" id="idx47">python3 -m venv .venv</line>
<line number="48" id="idx48">source .venv/bin/activate</line>
<line number="49" id="idx49">
```</line>
<line number="50" id="idx50"></line>
<line number="51" id="idx51">### Install & Initialize</line>
<line number="52" id="idx52">
```bash</line>
<line number="53" id="idx53">pip install -r requirements.txt</line>
<line number="54" id="idx54">cp .env.example .env</line>
<line number="55" id="idx55">python manage.py migrate</line>
<line number="56" id="idx56">
```</line>
<line number="57" id="idx57"></line>
<line number="58" id="idx58">### Run Server</line>
<line number="59" id="idx59">
```bash</line>
<line number="60" id="idx60">python manage.py runserver</line>
<line number="61" id="idx61">
```</line>
<line number="62" id="idx62"></line>
<line number="63" id="idx63">## 3. Running Background Workers</line>
<line number="64" id="idx64">To handle asynchronous tasks like sending SMS, start the Celery worker:</line>
<line number="65" id="idx65">
```bash</line>
<line number="66" id="idx66"># Start Worker</line>
<line number="67" id="idx67">celery -A core worker -l info</line>
<line number="68" id="idx68"></line>
<line number="69" id="idx69"># Start Beat (for scheduled tasks)</line>
<line number="70" id="idx70">celery -A core beat -l info</line>
<line number="71" id="idx71">
```</line>
<line number="72" id="idx72"></line>
<line number="73" id="idx73">## 4. Important Notes</line>
<line number="74" id="idx74">- 🛠 **Redis** must be running for OTP and Celery to function correctly.</line>
<line number="75" id="idx75">- 🔒 **Security**: The `.env` file is excluded from Git. Always update `.env.example` when adding new variables.</line>
<line number="76" id="idx76">- 📦 **Dependencies**: Keep your `requirements.txt` updated by running `pip freeze > requirements.txt`.</line>
<line number="77" id="idx77"></line>
<line number="78" id="idx78">## 5. License</line>
<line number="79" id="idx79">This project is currently for development and educational purposes.</line>
</canvas>
