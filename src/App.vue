<template>
  <post-header/>
  <!-- <post-db/> -->
  <post-content/>   
  <post-footer/>        
</template>

<script>

import PostHeader from './components/PostHeader.vue'
// import PostDb from './components/PostDb.vue'
import PostContent from './components/PostContent.vue'
import PostFooter from './components/PostFooter.vue'



export default {
  name: 'App',
  components: {
    PostHeader,
    // PostDb,
    PostContent,    
    PostFooter,   
  },    
}

</script>