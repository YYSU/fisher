from flask import Flask, current_app


app = Flask(__name__)

# Flask 內有兩種 context (Object)
# Application Context - Flask
# Request Context - Request

# Flask (核心對象，裡面保存配置文件的資訊、註冊路由、view function) --- 被封裝於 ---> AppContext 對象中
# Request （保存請求資訊、URL參數等等）--- 被封裝於 ---> RequestContext 對象中
# 若程式碼想存取上述 Flask or Request，我們應該使用 AppContext or RequestContext 間接的去操作
# 那為什麼我們先前都沒有去使用到這兩個 Context 呢？這是因為 current_app、request 中的 LocalProxy 幫我們實踐了

# current_app 裡面實際上是回應 AppContext 的 Flask (_app_ctx_stack.top 的 flask app)
# request 裡面實際上是回應 RequestContext 的 request (_request_ctx_stack.top 的 request)
"""
source code :
current_app: "Flask" = LocalProxy(_find_app)  # type: ignore
        .
        .
def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app

request: "Request" = LocalProxy(partial(_lookup_req_object, "request"))  # type: ignore
        .
        .
def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)
"""
# 然而為何之前在 spider/yushu裡面不需要手動 push context呢？因為在 request 進來時，會先檢查 app ctx stack，若沒有 context 存在
# 會幫忙push進去(由flask完成)

# 需要手動 push context的情況：單元測試、離線應用
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# print(d)
# ctx.pop()

# 改寫上面程式碼
# https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
# 對於實踐了上下文協議的對象可以使用 with
# __enter__ & __exit__ 實踐了左邊這兩個 func 代表為上下文管理器
# 上下文表達式必須要返回一個上下文管理器
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    print(d)
