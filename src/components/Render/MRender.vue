<!--
 * @Author: flwfdd
 * @Date: 2021-08-10 13:30:18
 * @LastEditTime: 2021-08-11 00:31:33
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-card>
    <v-container fluid>
      <v-row justify="center">
        <p style="font-size: 1.42rem" class="blue-grey--text text--darken-3 ma-2">{{ doc.title }}</p>
      </v-row>
      <v-row justify="center">
        <v-chip small class="ma-1" color="red" outlined>
          {{ doc.id }}
        </v-chip>
        <v-chip small class="ma-1" color="cyan" outlined>
          <v-icon left> account_circle </v-icon>
          {{ doc.user }}
        </v-chip>
        <v-chip small class="ma-1" color="purple" outlined>
          <v-icon left> bookmark </v-icon>
          {{ doc.tag }}
        </v-chip>
        <v-chip small class="ma-1" color="green" outlined>
          <v-icon left> note_add </v-icon>
          {{ format_first_time }}
        </v-chip>
        <v-chip small class="ma-1" color="orange" outlined>
          <v-icon left> edit </v-icon>
          {{ format_last_time }}
        </v-chip>
      </v-row>
      <br />
      <v-divider></v-divider>
      <m-render-item
        v-for="i in doc.blocks"
        :item="i"
        :key="i.id"
      ></m-render-item>
    </v-container>
  </v-card>
</template>

<script>
import MRenderItem from "./MRenderItem.vue";

export default {
  components: { MRenderItem },
  props: ["data","id"],
  data: () => ({
    doc: {
      id: -1,
      title: "",
      user: "",
      tag: "",
      first_time: 0,
      last_time: 0,
      blocks: [],
    },
  }),
  methods: {
    FormatDate(t) {
      var now = new Date(t * 1000);
      var year = now.getFullYear();
      var month = now.getMonth() + 1;
      var date = now.getDate();
      var hour = now.getHours();
      var minute = now.getMinutes();
      var second = now.getSeconds();
      return (
        year +
        "-" +
        month.toString().padStart(2,'0') +
        "-" +
        date.toString().padStart(2,'0') +
        " " +
        hour.toString().padStart(2,'0') +
        ":" +
        minute.toString().padStart(2,'0') +
        ":" +
        second.toString().padStart(2,'0')
      );
    },
    Get() {
      this.$axios
        .get(this.$axios.defaults.api + "/get_doc/?id=" + this.id)
        .then((res) => {
          this.doc = res.data;
          this.doc.blocks = JSON.parse(this.doc.blocks);
        })
        .catch((err) => {
          console.log("Get failed: ", err);
        });
    },
  },
  computed: {
    format_first_time() {
      return this.FormatDate(this.doc.first_time);
    },
    format_last_time() {
      return this.FormatDate(this.doc.last_time);
    },
  },
  created() {
    if(this.data){
      this.doc=this.data;
    }
    if (this.id) {
      this.Get(this.id);
    }
  },
};
</script>