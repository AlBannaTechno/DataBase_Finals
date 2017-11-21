"""
"مشروع التحكم في قاعدة البيانات وللععلم فهذا المشروع لن يتم استخدامه هنا
بل إنشاء المشروع الكامل في الملف CLDataBase=Current Load DataBase
"""

"إضافة المكتبة الخاصة بالعمل على قواعد البيانات"
import pypyodbc

class mdbconnecter():
    "الفئة المسؤلة عن التحكم في قواعد البيانات"
    def __init__(self,mdbpath,Cr=-1):
        "المشيد العام"
        "mdbpath : مسار قاعدة البيانات مشتملا على اسمها"
        "Cr :إنشاء قاعدة بيانات أو الاتصال بها فقط أو الاتصال ببها"
        "بعد إنشائها"
        """
        Cr=-1   : الاتصال بقاعدة البيانات
        Cr=0    : إنشاء قاعدة البيانات والاتصال بها
        Cr=-1   : إنشاء قاعدة البيانات فقط
        """
        if Cr==-1:
            self.conn = pypyodbc.win_connect_mdb(mdbpath)
        elif Cr==1:
            self.mymdb = pypyodbc.win_create_mdb(mdbpath)
        elif Cr==0:
            self.mymdb = pypyodbc.win_create_mdb(mdbpath)
            self.conn = pypyodbc.win_connect_mdb(mdbpath)
        "إنشاء المؤشر الذي يتحكم في قاعدة البيانات"
        self.cur = self.conn.cursor()
    def make_query_send(self,query,values):
        """دالة إرسال أمر الى قاعدة البيانات ولاكن هذا الامر لا يرجع أي قيم
والمدخل الأول يعبر عن الأمر المرسل الى قاعدة البيانات
بينما المدخل الثاني هو القيم التي يتم إرسالها
لأن البرنامج هنا يتعامل مع أوامر قاعدة البيانات كالتالي
query="insert into tablename(a1,a2,a3,....) values(?,?,?,....)
values_orAnyName=(23,43,54,234,...)
execute(query,values_orAnyName)
وللعلم فعلامة الاستفهام هي من التركيب النحوي syntax
للأمر المرسل لقاعدة البيبانات أي أنه لابد من ان يتم وضع علامات استفاه بدل أي متغير
        """
        self.cur.execute(query,values)
        "إرسال الأمر"
        ""
        self.conn.commit()
        "تأكيد التغييرات"
    def make_query_get(self,query):
        "دالة الحصول على قيم من قواعد البيانات"
        self.cur.execute(query)
        "إرسال الأمر"

        "إرجاع النواتج"
        return self.cur.fetchall()

    "البايقي هي بعض التعديلات الخاصة بالمهدم والتي لم تكتمل"
    def __enter__(self):
        return self

    def __exit__(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
