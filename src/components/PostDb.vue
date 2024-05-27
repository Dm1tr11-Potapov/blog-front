<template>       
    <div class="post-db">
        <div class="feedback">
            <p>FEEDBACK</p>
            <input type="text" v-model="item.name" placeholder="Name" style="height: 40px; font-size: 16px;">
            <input type="text" v-model="item.description" placeholder="Description" style="min-height: 40px; font-size: 16px;">
            <button @click="addComment" style="font-size: 20px; "  >Add Comment</button>
        </div>        
    
        <div class="items">
            <h2 style="text-align: center">Comments:</h2>           
            <ul>
                <li 
                    v-for="item in items" 
                    :key="item.id">
                    {{ item.name }}: {{ item.description }}
                </li>
            </ul>        
        </div>
        <hr>
    </div>
</template>

<script> 
import axios from 'axios';

export default {            
    props: {
        PostDb: Object},
        data() {
            return {
                item: { name: '', description: '' },
                items: []
            };
        },       
         
    
    created() {
        this.fetchItems();
    },
    methods: {      
        async addComment() {
            try {
                const response = await axios.post('http://127.0.0.1:8088/items/', this.item);
                console.log(response.data);                
                this.item = { name: '', description: '' };
            } catch (error) {
                console.error(error);
            }
        },
        async fetchItems() {
            try {
                const response = await axios.get('http://127.0.0.1:8088/items/');
                this.items = response.data;
            } catch (error) {
                console.error(error);
                this.items = [];
            }
        },    
    },
};

</script>

<style scoped>

.post-db{
    color:rgb(255, 255, 255);
    text-align: center;    
    align-items: center;
    margin: 0 auto;
    font-size: 20px;    
}
.feedback {
    background-color: rgb(126, 154, 244);
    font-size: 20px;
    display: grid;    
    margin-left: 25px;
    margin-right: 10px;
    margin-top: 25px;    
}
.items {
    margin-left: 25px;
    margin-top: 25px;
    color: black;
    display:block;
    text-align: left;   
    
}
</style>