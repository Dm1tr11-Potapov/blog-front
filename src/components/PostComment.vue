<template>
    <div class="comment">
        <p><strong>{{ comment.author }}</strong>: {{ comment.content }}</p>
    </div>
</template>

<script>
    export default {
        props:  {
            comment: Object
        }
    }
</script>