<html>
<title>用户注册</title>
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
<div class="uk-width-2-3">
        <h1>欢迎注册！</h1>
        <form id="form-register" v-on="submit: submit" class="uk-form uk-form-stacked">
            <div class="uk-alert uk-alert-danger uk-hidden"></div>
            <div class="uk-form-row">
                <label class="uk-form-label">名字:</label>
                <div class="uk-form-controls">
                    <input v-model="name" type="text" maxlength="50" placeholder="名字" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">电子邮件:</label>
                <div class="uk-form-controls">
                    <input v-model="email" type="text" maxlength="50" placeholder="your-name@example.com" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">输入口令:</label>
                <div class="uk-form-controls">
                    <input v-model="password1" type="password" maxlength="50" placeholder="输入口令" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <label class="uk-form-label">重复口令:</label>
                <div class="uk-form-controls">
                    <input v-model="password2" type="password" maxlength="50" placeholder="重复口令" class="uk-width-1-1">
                </div>
            </div>
            <div class="uk-form-row">
                <button type="submit" class="uk-button uk-button-primary"><i class="uk-icon-user"></i> 注册</button>
            </div>
        </form>
    </div>
</html>