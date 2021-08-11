<!--
 * @Author: flwfdd
 * @Date: 2021-08-10 16:34:45
 * @LastEditTime: 2021-08-11 10:42:47
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-container fluid>
    <v-btn fab bottom right fixed color="green" dark @click="Go('Editor')"
      ><v-icon>add</v-icon></v-btn
    >
    <p class="text-center blue-grey--text ma-n4" style="font-size: 4.2rem">
      记忆
    </p>
    <v-text-field
      dense
      outlined
      color="cyan"
      label="搜索"
      v-model="search"
      append-icon="search"
      @click:append="
        list = [];
        offset = 0;
        Get();
      "
    >
    </v-text-field>

    <v-card v-for="i in list" :key="i.id" class="my-4" outlined>
      <p
        class="text-center ma-2 blue-grey--text text--darken-2"
        style="font-size: 1.42rem"
      >
        {{ i.title }}
      </p>
      <v-card-text class="py-0 text-center">
        {{ i.user }} | {{ i.tag }} | {{ FormatDate(i.first_time) }} |
        {{ FormatDate(i.last_time) }}
        <!-- <v-chip small class="mx-1" color="cyan" outlined>
          <v-icon left> account_circle </v-icon>
          {{ i.user }}
        </v-chip>
        <v-chip small class="mx-1" color="purple" outlined>
          <v-icon left> bookmark </v-icon>
          {{ i.tag }}
        </v-chip>
      </v-card-text>
      <v-card-text class="py-0 text-center">
        <v-chip small class="mx-1" color="green" outlined>
          <v-icon left> note_add </v-icon>
          {{ FormatDate(i.first_time) }}
        </v-chip>
        <v-chip small class="mx-1" color="orange" outlined>
          <v-icon left> edit </v-icon>
          {{ FormatDate(i.last_time) }}
        </v-chip> -->
      </v-card-text>
      <v-card-text class="py-1 text-center">
        <v-btn
          outlined
          class="mx-1"
          color="cyan"
          @click="Go('/Render?id=' + i.id)"
          >查看</v-btn
        >
        <v-btn
          outlined
          class="mx-1"
          color="purple"
          @click="Go('/Editor?id=' + i.id)"
          >编辑</v-btn
        >
      </v-card-text>
    </v-card>
    <v-btn @click="Get" block color="green" outlined>更多</v-btn>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    list: [],
    offset: 0,
    limit: 24,
    search: "",
  }),
  methods: {
    Get() {
      this.$axios
        .get(this.$axios.defaults.api + "/get_doc_list/", {
          params: {
            offset: this.offset,
            limit: this.limit,
            search: this.search,
          },
        })
        .then((res) => {
          this.list = this.list.concat(res.data.list);
          this.offset += this.limit;
        })
        .catch((err) => {
          console.log("Get failed: ", err);
        });
    },
    Go(url) {
      this.$router.push(url);
    },
    FormatDate(t) {
      var now = new Date(t * 1000);
      var year = now.getFullYear();
      var month = now.getMonth() + 1;
      var date = now.getDate();
      return (
        year +
        "-" +
        month.toString().padStart(2, "0") +
        "-" +
        date.toString().padStart(2, "0")
      );
    },
  },
  created() {
    this.Get();
  },
};
</script>