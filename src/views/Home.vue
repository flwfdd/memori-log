<!--
 * @Author: flwfdd
 * @Date: 2021-08-04 23:19:33
 * @LastEditTime: 2021-08-05 22:24:18
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="4">
        <v-img src="../assets/memori.png"></v-img>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col class="text-center">
        <h1 class="light-blue--text">memori</h1>
        <h6><b class="light-blue--text">mem</b>ory with <b class="blue--text">ori</b>gin</h6>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col class="text-center blue-grey--text">
        <h4>{{hitokoto}}</h4>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Home",
  data:()=>({
    hitokoto:"",
  }),
  methods: {
    UpHitokoto() {
      this.$axios.get("https://v1.hitokoto.cn/")
      .then(res=>{
        this.hitokoto = res.data.hitokoto + "  ——" + res.data.from;
      });
    },
  },
  created(){
    this.UpHitokoto();
    setInterval(this.UpHitokoto,10*1000);
  }
};
</script>
