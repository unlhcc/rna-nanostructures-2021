<template>
  <b-form-select
    :id="id"
    v-model="data"
    :options="options"
    stacked
    :disabled="readOnly"
    :state="componentValidState"
    @input="valueChanged"
  />
</template>

<script>
import { InputEditorMixin } from "django-airavata-workspace-plugin-api";

const CONFIG_OPTION_TEXT_KEY = "text";
const CONFIG_OPTION_VALUE_KEY = "value";

export default {
  name: "select-input-editor",
  mixins: [InputEditorMixin],
  props: {
    value: {
      type: String,
    },
  },
  computed: {
    options: function () {
      return "options" in this.editorConfig
        ? this.editorConfig["options"].map((option) => {
            return {
              text: option[CONFIG_OPTION_TEXT_KEY],
              value: option[CONFIG_OPTION_VALUE_KEY],
            };
          })
        : [];
    },
  },
};
</script>
