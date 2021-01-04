import trevignano_2016 from '../js/trevignano_2016.js';
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
      trevignano_2016: trevignano_2016,
      trevignano: trevignano
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
      if (year == "2016") {      
        this.prophecies = this.trevignano_2016.filter(prophecy => {
        return prophecy.month_string.includes("January")
        })
      }
      else if (year == "2017") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")
        })
      }
      else if (year == "2018") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")
        })
      }

      else if (year == "2019") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")
        })
      }

      else if (year == "2020") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")
        })
      }

      else {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes("January")
        })

      }



    },
    getProphecies(year, month) {
      this.month = month;
      if (year == "2016") {      
        this.prophecies = this.trevignano_2016.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })
      }
      else if (year == "2017") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)
        })
      }
      else if (year == "2018") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)
        })
      }

      else if (year == "2019") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)
        })
      }

      else if (year == "2020") {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)
        })
      }

      else {
        this.prophecies = this.trevignano.filter(prophecy => {
        return prophecy.year.includes(year) && prophecy.month_string.includes(month)
        })

      }
    }
  },
  mounted () {
  },
  created() {
    this.getProphecies('2020', 'January')
  }
})



