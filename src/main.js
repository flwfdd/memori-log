/*
 * @Author: flwfdd
 * @Date: 2021-07-15 10:56:23
 * @LastEditTime: 2021-08-07 01:20:32
 * @Description: 
 * _(:з」∠)_
 */
import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$axios=axios
axios.defaults.api="http://memori.flwfdd.xyz/api"

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
