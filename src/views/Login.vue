<!--
 * @Author: flwfdd
 * @Date: 2021-08-06 23:39:33
 * @LastEditTime: 2021-08-07 00:36:56
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-container>
    <v-card class="ma-5">
      <v-card-text>
        <v-alert v-if="ok == -1" text color="blue" class="text-center"
          >未登录</v-alert
        >
        <v-alert v-else-if="ok == 1" text color="green" class="text-center"
          >已登录</v-alert
        >
        <v-alert v-else text color="red" class="text-center">登陆失败</v-alert>

        <v-text-field
          color="cyan"
          outlined
          v-model="user"
          label="你的名字。"
        ></v-text-field>
        <v-text-field
          color="cyan"
          outlined
          v-model="password"
          label="你的密码。"
        ></v-text-field>

        <v-btn block outlined color="cyan" @click="Login">登陆</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    user: "",
    password: "",
    ok: -1,
  }),
  methods: {
    Login() {
      document.cookie="user="+this.user+";expires="+new Date(new Date().getTime()+30*24*3600*1000).toGMTString();
      document.cookie="key="+this.user+this.password+";expires="+new Date(new Date().getTime()+30*24*3600*1000).toGMTString();
      this.CheckLogin();
    },
    CheckLogin() {
      this.$axios
        .get(this.$axios.defaults.api + "/check_login/")
        .then(() => {
          this.ok = 1;
        })
        .catch(() => {
          this.ok = -1;
        });
    },
  },
  created(){
      this.CheckLogin();
  }
};
</script>