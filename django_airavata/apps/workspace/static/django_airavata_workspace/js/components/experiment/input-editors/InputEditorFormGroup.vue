// Do not add whitespaces for feedback and feedbackMessages.
// Using the style to preserve whitespaces from error messages
// due to vue 3 limitations.
<template>
  <b-form-group
    :label="label"
    :label-for="labelFor"
    :state="state"
    :description="description"
  >
    <slot></slot>
    <template slot="invalid-feedback">
      <ul v-if="feedbackMessages && feedbackMessages.length > 1">
        <li v-for="feedback in feedbackMessages" :key="feedback" style="white-space: pre-wrap;">{{ feedback }}</li>
      </ul>
      <div v-else-if="feedbackMessages && feedbackMessages.length === 1" style="white-space: pre-wrap;">{{ feedbackMessages[0] }}</div>
    </template>
    <linkify slot="description">{{ description }}</linkify>
  </b-form-group>
</template>

<script>
import { components } from "django-airavata-common-ui";
export default {
  name: "input-editor-form-group",
  props: {
    label: {
      type: String,
      required: true
    },
    labelFor: {
      type: String,
      required: true
    },
    state: {
      type: String
    },
    feedbackMessages: {
      type: Array
    },
    description: {
      type: String
    }
  },
  components: {
    linkify: components.Linkify
  }
};
</script>
