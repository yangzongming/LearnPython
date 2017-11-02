<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>欢迎注册</title>
    <link rel="stylesheet" href="http://127.0.0.1:8000/static/css/uikit.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:8000/static/css/uikit.gradient.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:8000/static/css/awesome.css"/>
    <script src="http://127.0.0.1:8000/static/js/jquery.min.js"></script>
    <script src="http://127.0.0.1:8000/static/js/md5.js"></script>
    <script src="http://127.0.0.1:8000/static/js/uikit.min.js"></script>
    <script src="http://127.0.0.1:8000/static/js/sticky.min.js"></script>
    <script src="http://127.0.0.1:8000/static/js/vue.min.js"></script>
    <script src="http://127.0.0.1:8000/static/js/awesome.js"></script>
</head>
<body>
<script>
function validateEmail(email) {
    var re = /^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$/;
    return re.test(email.toLowerCase());
}
$(function () {
    var vm = new Vue({
        el: '#form-register',
        data: {
            name: '',
            email: '',
            password1: '',
            password2: ''
        },
        methods: {
            submit: function (event) {
                event.preventDefault();
                if (! this.name.trim()) {
                    return showError('请输入名字');
                }
                if (! validateEmail(this.email.trim().toLowerCase())) {
                    return showError('请输入正确的Email地址');
                }
                if (this.password1.length < 6) {
                    return showError('口令长度至少为6个字符');
                }
                if (this.password1 !== this.password2) {
                    return showError('两次输入的口令不一致');
                }
                startLoading();
                postApi('/api/users', {
                    name: this.name,
                    email: this.email.trim().toLowerCase(),
                    password: CryptoJS.MD5(this.password1).toString(),
                }, function (err, r) {
                    if (err) {
                        showError(err);
                    }
                    else {
                        return location.assign('/');
                    }
                    stopLoading();
                });
            }
        }
    });
});
</script>
<p><h2>管理员登陆</h2></p>
        <form action="/register" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
</body>
</html>