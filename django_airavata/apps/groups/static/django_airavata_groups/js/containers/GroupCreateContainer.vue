<template>
  <group-editor :group="newGroup" @saved="handleSaved"></group-editor>
</template>

<script>
import GroupEditor from "../group_components/GroupEditor.vue";

import { models, session } from "django-airavata-api";
export default {
  name: "group-create-container",
  data() {
    return {
      newGroup: this.createNewGroup(),
    };
  },
  components: {
    GroupEditor,
  },
  methods: {
    handleSaved: function () {
      window.location.assign("/groups/");
    },
    createNewGroup() {
      const group = new models.Group();
      const ownerId = session.Session.airavataInternalUserId;
      group.members.push(ownerId);
      group.ownerId = ownerId;
      return group;
    },
  },
  computed: {},
  beforeMount: function () {},
};
</script>
