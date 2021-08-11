<!--
 * @Author: flwfdd
 * @Date: 2021-08-10 17:52:50
 * @LastEditTime: 2021-08-10 22:38:15
 * @Description: 
 * _(:з」∠)_
-->

<template>
  <v-container fluid>
    <v-btn block outlined color="green" @click="GetBefore">上一章</v-btn>
    <m-render v-for="i in ids" :id="i" :key="i" class="my-4"></m-render>
    <v-btn block outlined color="green" @click="GetAfter">下一章</v-btn>
  </v-container>
</template>

<script>
import MRender from "../components/Render/MRender.vue";
export default {
  components: {
    MRender,
  },
  data: () => ({
    ids: [],
  }),
  methods: {
    GetBefore() {
      if (this.ids[0] > 1) this.ids.splice(0, 0, this.ids[0] - 1);
    },
    GetAfter() {
      this.ids.push(Number(this.ids[this.ids.length-1]) + 1);
    },
  },
  created() {
    this.ids.push(this.$route.query.id);
  },
};
</script>