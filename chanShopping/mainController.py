import os
import urllib.request
import urllib.parse

from functools import wraps

import requests
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login  import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from python.api.naverAPI import NaverAPI
from python.form.loginForm import LoginForm
from python.form.registerForm import RegisterForm
from python.form.findIdForm import FindIdForm
from python.form.findPassForm import FindPassForm
from python.mail.sendMail import SendMail
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

api = NaverAPI()
mail = SendMail()

item_id = [i for i in range(1,51)]

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.Integer,nullable=False)
    title = db.Column(db.String(500),nullable=False)
    link = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    price = db.Column(db.String(250), nullable=False)
    count = db.Column(db.Integer, nullable=False)


class User(UserMixin,db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250),nullable=False)
    id = db.Column(db.String(250),nullable=False)
    password = db.Column(db.String(250),nullable=False)


class Comment(db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    item_id = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.String(250),nullable=False)
    date = db.Column(db.String(100),nullable=False)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(250),nullable=False)


class Address(db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(100),nullable=False)
    address_number = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String(250),nullable=False)
    address_detail = db.Column(db.String(250),nullable=False)
    reference = db.Column(db.String(250),nullable=False)


class Purchase(db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    address_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(250), nullable=False)
    address_detail = db.Column(db.String(250), nullable=False)
    reference = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250),nullable=False)


class  Basket(db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(250),nullable=False)
    item_id = db.Column(db.Integer,nullable=False)


class Love(db.Model):
    primary_key = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(250),nullable=False)
    item_id = db.Column(db.Integer,nullable=False)
    date = db.Column(db.String(250),nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def login_Required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("loginPage"))
        return f(*args,**kwargs)
    return decorated_function


@app.route("/")
def web_start():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for("mainPage"))


@app.route("/main")
def mainPage():
    item_list = []
    galaxy_phone = Item.query.filter_by(category=1).all()
    Iphone = Item.query.filter_by(category=2).all()
    galaxy_book = Item.query.filter_by(category=3).all()
    mac_book = Item.query.filter_by(category=4).all()
    desktop = Item.query.filter_by(category=5).all()

    item_list.append(galaxy_phone)
    item_list.append(Iphone)
    item_list.append(galaxy_book)
    item_list.append(mac_book)
    item_list.append(desktop)

    purchase_list = Purchase.query.filter_by().all()
    purchase_check = [{f"{i}" : 0} for i in range(1,51)]
    for item in purchase_list:
        if item.item_id in item_id:
            purchase_check[item.item_id-1][f"{item.item_id}"] += 1
    sorted_list = sorted(purchase_check, key=lambda x: list(x.values())[0], reverse=True)
    sorted_keys = [list(item.keys())[0] for item in sorted_list]
    popular_list = []
    for i in range(0,4):
        popular_list.append(Item.query.filter_by(id=int(sorted_keys[i])).first())


    review_list = Comment.query.filter_by().all()
    review_check = [{"item_id": i, "score" : 0 , "count" : 0 ,"average" : 0.0 } for i in range(1,51)]
    for review in review_list:
        if review.item_id in item_id:
            review_check[review.item_id-1]["count"] += 1
            review_check[review.item_id-1]["score"] += review.score
    for review in review_check:
        if review["count"] != 0:
            review["average"] = review["score"] / review["count"]
    sorted_list = sorted(review_check,key=lambda x: list(x.values())[3],reverse=True)
    sorted_keys = [list(item.values())[0] for item in sorted_list]
    review_score_list = []
    for i in range(0,4):
        review_score_list.append(Item.query.filter_by(id=int(sorted_keys[i])).first())

    logged = current_user.is_authenticated
    return render_template("main.html",items=item_list,logged=logged,current_user=current_user,popular_list=popular_list,review_score_list=review_score_list)


@app.route("/search",methods=["GET","POST"])
def searchPage():
    if request.method == "POST":
        keyword = request.form.get("search_keyword")
        items = api.searchItem(keyword)

        if not items:
            items_length = 0
        else:
            for item in items:
                item["title"] = item["title"].replace("<b>","").replace("</b>","")
            items_length = len(items)

    logged = current_user.is_authenticated
    return render_template("/product/search.html",logged=logged,current_user=current_user,items=items,items_length=items_length,keyword=keyword)


@app.route("/user/<int:id>")
@login_Required
def userPage(id):
    logged = current_user.is_authenticated
    user_address = Address.query.filter_by(user_id=current_user.id).first()

    return render_template("/member/user.html",logged=logged,current_user=current_user,item_id=id,user_address=user_address)


@app.route("/address_register",methods=["POST"])
@login_Required
def address_register():
    address_number = request.form["address_number"]
    address = request.form["address"]
    address_detail = request.form["address_detail"]
    reference = request.form["reference"]
    item_id = request.form["id"]

    user_address = Address.query.filter_by(user_id=current_user.id).first()
    print(user_address)
    if user_address:
        user_address.address_number = address_number
        user_address.address = address
        user_address.address_detail = address_detail
        user_address.reference = reference
        db.session.commit()
        flash("주소 수정이 완료되었습니다!")
    else:
        new_address = Address(address_number=address_number,address=address,address_detail=address_detail,reference=reference,
                              user_id=current_user.id)

        db.session.add(new_address)
        db.session.commit()
        flash("주소 등록이 완료되었습니다!")
    return redirect(url_for("userPage",id=item_id))


@app.route("/category/<int:num>")
def categoryPage(num):
    item_list = Item.query.filter_by(category=num).all()
    category_dict = {
        1 : "Galaxy Phone",
        2 : "Iphone",
        3 : "Galaxy Book",
        4 : "Mac Book",
        5 : "Desktop"
    }
    category = category_dict[num]
    logged = current_user.is_authenticated
    comment_json = []
    for item in item_list:
        id = item.id
        comment_list = Comment.query.filter_by(item_id=id).all()
        score_list = Comment.query.filter_by(item_id=id).all()

        score = 0
        comment_length = len(comment_list)
        average = 0
        if not len(score_list) == 0:
            for item_score in score_list:
                score += item_score.score
            average = round(score / len(score_list),1)
        comment_data = {
            "average" : average,
            "comment_length" : comment_length
        }
        comment_json.append(comment_data)
    return render_template("product/category.html",items=item_list,category=category,comment=comment_json,logged=logged, current_user=current_user)



@app.route("/detail/<int:id>")
@login_Required
def detailPage(id):
    item = Item.query.filter_by(id=id).first()
    category_num = item.id // 10
    category_dict = {
        0: "Galaxy Phone",
        1: "Iphone",
        2: "Galaxy Book",
        3: "Mac Book",
        4: "Desktop"
    }
    comment_list = Comment.query.filter_by(item_id=id).all()
    score_list = Comment.query.filter_by(item_id=id).all()

    score = 0
    average = 0
    if not len(score_list) == 0:
        for item_score in score_list:
            score += item_score.score
        average = round(score / len(score_list),1)

    category = category_dict[category_num]
    logged = current_user.is_authenticated

    return render_template("/product/detail.html",item=item,current_user=current_user,logged=logged,category=category,
                           comment_length=len(comment_list),average=average)


@app.route("/login",methods=["GET","POST"])
def loginPage():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        id = loginForm.id.data
        password = loginForm.password.data

        user = User.query.filter_by(id=id,password=password).first()
        if user:
            login_user(user)
            return redirect(url_for("mainPage"))
        else:
            flash("로그인 정보가 일치하지 않습니다. 다시 로그인해주세요.")
            return redirect(url_for("loginPage"))

    return render_template("/member/login.html",form=loginForm)


@app.route('/logout')
@login_Required
def logout():
    logout_user()
    flash("로그아웃 되었습니다!")
    return redirect(url_for('mainPage'))


@app.route("/id_duplicated",methods=["POST"])
def id_duplicated():
    json_data = request.get_json()
    id = json_data["id"]
    duplicated_id = User.query.filter_by(id=id).first()
    if duplicated_id:
        return "duplicated"
    else:
        return "nonDuplicated"



@app.route("/register",methods=["GET","POST"])
def registerPage():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        name = registerForm.name.data
        email = registerForm.email.data
        id = registerForm.id.data
        password = registerForm.password.data

        new_user = User(name=name,email=email,id=id,password=password)
        db.session.add(new_user)
        db.session.commit()
        print("Register Success")
        return redirect(url_for("loginPage"))

    return render_template("member/register.html",form=registerForm)



@app.route("/find_id",methods=["GET","POST"])
def findIdPage():
    findIdForm = FindIdForm()
    if request.method == "POST":
        json_data = request.get_json()
        name = json_data["name"]
        email = json_data["email"]
        user = User.query.filter_by(name=name,email=email).all()
        if user:
            id_list = [ids.id for ids in user]
            return id_list
        else:
            return "None"
    return render_template("member/find_id.html",form=findIdForm)



@app.route("/find_pass",methods=["GET","POST"])
def findPassPage():
    findPassForm = FindPassForm()
    if request.method == "POST":
        json_data = request.get_json()
        id = json_data["id"]

        user = User.query.filter_by(id=id).first()
        if user:
            return user.password
        else:
            return "None"
    return render_template("member/find_pass.html",form=findPassForm)



@app.route("/mail",methods=["POST"])
def sendMail():
    json_data = request.get_json()
    email = json_data["email"]
    generate_string = mail.sendMessage(email)
    return generate_string


@app.route("/kakaopay/<int:id>", methods=["GET"])
@login_Required
def paymentPage(id):
    item = Item.query.filter_by(id=id).first()
    category_num = item.id // 10
    category_dict = {
        0: "Galaxy Phone",
        1: "Iphone",
        2: "Galaxy Book",
        3: "Mac Book",
        4: "Desktop"
    }
    item = Item.query.filter_by(id=id).first()
    address = Address.query.filter_by(user_id=current_user.id).first()

    category = category_dict[category_num]
    logged = current_user.is_authenticated
    return render_template("/kakaopay/payment.html",item=item,logged=logged,current_user=current_user,category=category,address=address)


@app.route("/kakaopay/paymethod.ajax", methods=['POST'])
@login_Required
def paymethod():
    if request.method == 'POST':
        json_data = request.get_json()
        item_id = json_data["id"]
        quantity = int(json_data["quantity"])
        item = Item.query.filter_by(id=item_id).first()

        item_price = item.price.replace(",","")
        total_price = int(item_price) * quantity
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': "KakaoAK " + os.getenv("KAKAO_APP_KEY"), # admin_key
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8", # 보내는 형식
        }
        params = {
            "cid": "TC0ONETIME", # test용 코드(가맹점코드)
            "partner_order_id": "chan", # 가맹점 주문 코드
            "partner_user_id": "오규찬", # 가맹점 회원
            "item_name": f"{item.title}", # 상품명
            "quantity": quantity,  # 상품수량
            "total_amount": f"{total_price}", # 총 가격
            "tax_free_amount": 0, # 상품 비과세 금액
            "vat_amount" : 200, # 상품 부과세 금액
            "approval_url": "http://127.0.0.1:5000/kakaopay/success", # 결제 성공식 redirect URL
            "cancel_url": "http://127.0.0.1:5000/kakaopay/cancel", # 결체 취소 시 redirect URL
            "fail_url": "http://127.0.0.1:5000/kakaopay/fail", # 결제 실패 시 redirect URL
        }

        res = requests.post(URL, headers=headers, params=params) # 결제 준비
        print(res.json())
        app.tib = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장

        return jsonify({'next_url': res.json()['next_redirect_pc_url']}) # 결제 전송

    return render_template('main.html')



@app.route("/kakaopay/success", methods=['POST', 'GET'])
@login_Required
def success():
    new_purchase_item = Purchase(user_id=current_user.id, item_id=session["item_id"], quantity=session["quantity"],
                                 address_number=session["address_number"],
                                 address=session["address"], address_detail=session["address_detail"], reference=session["reference"], date=session["current_date"])

    buy_item = Item.query.filter_by(id=session["item_id"]).first()
    buy_item.count -= session["quantity"]
    db.session.add(new_purchase_item)
    db.session.commit()

    session.pop("item_id")
    session.pop("quantity")
    session.pop("address_number")
    session.pop("address")
    session.pop("address_detail")
    session.pop("reference")
    session.pop("current_date")

    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + os.getenv("KAKAO_APP_KEY"),
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",  # 테스트용 코드
        "tid": app.tib,  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "chan",  # 주문번호
        "partner_user_id": "오규찬",  # 유저 아이디
        "pg_token": request.args.get("pg_token"),  # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    print(res)
    print(res.text)
    print(res.json())
    print(res.json()['amount'])
    print(res.json()['amount']['total'])
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }

    logged = current_user.is_authenticated

    return render_template('kakaopay/success.html', context=context, res=res,logged=logged,current_user=current_user,item=buy_item,purchase=new_purchase_item)


@app.route("/kakaopay/cancel", methods=['POST', 'GET'])
@login_Required
def cancel():
    session.pop("item_id")
    session.pop("quantity")
    session.pop("address_number")
    session.pop("address")
    session.pop("address_detail")
    session.pop("reference")
    session.pop("current_date")

    URL = "https://kapi.kakao.com/v1/payment/order"
    headers = {
        "Authorization": "KakaoAK " + os.getenv("KAKAO_APP_KEY"),
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",  # 가맹점 코드
        "tid": app.tib,  # 결제 고유 코드
    }

    res = requests.post(URL, headers=headers, params=params)
    print(res.text)
    amount = res.json()['cancel_available_amount']['total']
    context = {
        'res': res,
        'cancel_available_amount': amount,
    }

    if res.json()['status'] == "QUIT_PAYMENT":
        res = res.json()
        return render_template('kakaopay/cancel.html', params=params, res=res, context=context)



@app.route("/kakaopay/fail", methods=['POST', 'GET'])
@login_Required
def fail():
    session.pop("item_id")
    session.pop("quantity")
    session.pop("address_number")
    session.pop("address")
    session.pop("address_detail")
    session.pop("reference")
    session.pop("current_date")
    return render_template('fail.html')


@app.route("/review/<int:id>",methods=["GET"])
@login_Required
def reviewPage(id):
    comment_list = Comment.query.filter_by(item_id=id).all()
    score_list = Comment.query.filter_by(item_id=id).all()
    item = Item.query.filter_by(id=id).first()

    score = 0
    average = 0
    if not len(score_list) == 0:
        for item_score in score_list:
            score += item_score.score
        average = round(score / len(score_list),1)

    comment_length = len(comment_list)
    logged = current_user.is_authenticated
    return render_template("/review/review.html",logged=logged,current_user=current_user,average=average,
                           comments=comment_list,comment_length=comment_length,item=item)



@app.route("/review/writePage/<int:item_id>")
def reviewWritePage(item_id):
    item = Item.query.filter_by(id=item_id).first()
    logged = current_user.is_authenticated
    return render_template("/review/reviewWrite.html",logged=logged,current_user=current_user,item_id=item_id,item=item)


@app.route("/review/register",methods=["POST"])
def reviewRegister():
    if request.method == "POST":
        json_data = request.get_json()
        score = int(json_data["score"])
        text = json_data["text"]
        item_id = int(json_data["item_id"])
        date = dt.datetime.now().strftime("%Y.%m.%d")
        user_id = current_user.id

        new_comment = Comment(user_id=user_id,item_id=item_id,score=score,text=text,date=date)
        db.session.add(new_comment)
        db.session.commit()
        return "success"


@app.route("/buyProduct",methods=["POST"])
@login_Required
def buyProduct():
    if request.method == "POST":
        json_data = request.get_json()
        session["address_number"] = int(json_data["address_number"])
        session["address"] = json_data["address"]
        session["address_detail"] = json_data["address_detail"]
        session["reference"] = json_data["reference"]
        session["item_id"] = int(json_data["item_id"])
        session["quantity"] = int(json_data["quantity"])
        session["current_date"] = dt.datetime.now().strftime("%Y-%m-%d")
        return "success"



@app.route("/basket")
@login_Required
def basketPage():
    basket_list = Basket.query.filter_by(user_id=current_user.id).all()
    item_list = []
    for item in basket_list:
        item_list.append(Item.query.filter_by(id=item.item_id).first())

    date = dt.datetime.now().strftime("%m.%d")
    address = Address.query.filter_by(user_id=current_user.id).first()

    logged = current_user.is_authenticated
    return render_template("/myProduct/basket.html",logged=logged,current_user=current_user,items=item_list,date=date,address=address)



@app.route("/basket/register/<int:item_id>")
@login_Required
def basketRegister(item_id):
    check_basket = Basket.query.filter_by(user_id=current_user.id,item_id=item_id).first()
    if check_basket:
        flash("이미 장바구니에 등록되어있습니다.")
        return redirect(url_for("detailPage", id=item_id))
    new_basket = Basket(user_id=current_user.id,item_id=item_id)
    db.session.add(new_basket)
    db.session.commit()
    flash("장바구니 등록되었습니다!")
    return redirect(url_for("detailPage",id=item_id))


@app.route("/basket/delete",methods=["POST"])
@login_Required
def basketDelete():
    if request.method == "POST":
        json_data = request.get_json()
        delete_list = json_data["delete_id"]

        for id in delete_list:
            delete_item = Basket.query.filter_by(user_id=current_user.id,item_id=int(id)).first()
            db.session.delete(delete_item)
            db.session.commit()
    return "success"


@app.route("/buyList")
@login_Required
def buyListPage():
    current_user_id = current_user.id
    buy_items = Purchase.query.filter_by(user_id=current_user_id).all()
    items_list = []
    for item in buy_items:
        item_dic = {
            "item_info" : Item.query.filter_by(id=item.item_id).first(),
            "buy_info" : item
        }
        items_list.append(item_dic)

    logged = current_user.is_authenticated
    return render_template("/myProduct/buyList.html", logged=logged, current_user=current_user,items=items_list)


@app.route("/myList")
@login_Required
def myListPage():
    love_items = Love.query.filter_by(user_id=current_user.id).all()
    items_list = []
    for item in love_items:
        date = item.date
        item_dic = {
            "item" :  Item.query.filter_by(id=item.item_id).first(),
            "date" : date
        }
        items_list.append(item_dic)

    logged = current_user.is_authenticated
    return render_template("/myProduct/myList.html", logged=logged, current_user=current_user,items=items_list)


@app.route("/myList/love/<int:item_id>")
@login_Required
def myListRegister(item_id):
    check_love = Love.query.filter_by(user_id=current_user.id,item_id=item_id).first()
    if check_love:
        flash("이미 찜 목록에 등록되어있습니다.")
        return redirect(url_for("detailPage", id=item_id))
    date = dt.datetime.now().strftime("%Y.%m.%d")
    new_love = Love(user_id=current_user.id,item_id=item_id,date=date)

    db.session.add(new_love)
    db.session.commit()

    flash("찜 목록에 등록되었습니다.")
    return redirect(url_for("detailPage",id=item_id))


@app.route("/myList/delete/<int:item_id>")
def deleteMyList(item_id):
    item = Love.query.filter_by(item_id=item_id,user_id=current_user.id).first()
    db.session.delete(item)
    db.session.commit()
    flash("찜 목록에서 해제되었습니다!")
    return redirect(url_for("myListPage"))


if __name__ == "__main__":
    app.run(debug=True)


