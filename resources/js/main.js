import trevignano from '../js/trevignano.js';


new Vue({
  el: '#app',
  components: {


  },
  data () {
    return {
      search: '',
      year: "2021",
      month: "January",
      lang: "en",
      prophecies: [],
      trevignano: trevignano,
    }
  },
  computed: {

  },
  methods: {
    setLanguage(lang) {
      this.lang = lang
    },
    setYear(year) {
      this.year = year
      this.month = "January"
      this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")

      })
    },
    getProphecies(year, month) {
      this.month = month;
      this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)

      })
    }
  },
  mounted () {
  },
  created() {
    this.getProphecies('2020', 'January')
  }
})



