<script>
    let app = new Vue({
        el: '#app',
        delimiters: ['[[',']]'],
        data: {
            csrf_token: "",
            words: [],
            lists: [],
            users: [],
            },
        methods: {
            getWords()  {
                axios({
                    method: "get",
                    // FIND THIS URL
                    url: "/api/v1/"  
                }).then(response => this.words = response.data)   
            },
            getUserList() {
                axios({
                    method: "get",
                    url: "api/v1/users/"
                }).then(response => this.users = response.data)
                ;
            },
            createList() {
                axios({
                    method: "post",
                    url: "/api/v1/",
                    data: this.input,
                    headers: {
                        "X-CSRFToken": this.csrf_token
                        }
                }).then(response => {
                    this.newList = {
                        "creator": "",
                        "title": "",
                        "words": [],
                    }
                    this.getWords
                }).catch(error => {
                    let message = error.response.statusText;
                    for (let key in error.response.data) {
                        message += `\n${key}: $
                        {error.response.data[key]}`;
                    };
                    alert(message);
                })
            }
        },
        mounted: function() {
            this.csrf_token = document.querySelector("input [name=csrfmiddlewaretoken]").value;
            this.getWords();
            this.getUserList();
        }
        });
    </script>