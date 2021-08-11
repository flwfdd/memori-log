<!--
 * @Author: flwfdd
 * @Date: 2021-08-10 14:04:13
 * @LastEditTime: 2021-08-10 16:25:29
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <div>
    <v-card-text
      v-if="item.type == 'paragraph'"
      class="blue-grey--text text--darken-2"
      style="font-size: 1.05rem"
      v-html="item.data.text"
    >
    </v-card-text>

    <v-card v-else-if="item.type == 'image'" class="text-center ma-2" outlined>
      <v-img
        @click="Jump(item.data.file.url)"
        :src="item.data.file.url"
      ></v-img>
      <v-card-text v-html="item.data.caption"></v-card-text>
    </v-card>

    <v-card v-else-if="item.type == 'quote'" class="ma-2" outlined>
      <p
        class="mb-n12 ml-n4 mt-0 mr-0 pa-0 grey--text"
        style="font-size: 2.4rem"
      >
        “
      </p>
      <v-card-text
        v-html="item.data.text"
        class="blue-grey--text text--darken-2"
        style="font-size: 1.24rem"
      ></v-card-text>
      <p
        class="mt-n8 mr-n4 mb-n6 ml-0 pa-0 grey--text text-right"
        style="font-size: 2.4rem"
      >
        ”
      </p>
      <v-card-text class="ma-0 py-0">
        <v-divider></v-divider>
      </v-card-text>
      <v-card-text
        v-html="item.data.caption"
        class="text-right"
        style="font-size: 1.05rem"
      ></v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: ["item"],
  methods: {
    Jump(url) {
      window.open(url, "_blank");
    },
  },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>