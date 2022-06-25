import trevignano_2016 from '../js/trevignano2016.js';
import trevignano_2017 from '../js/trevignano2017.js';
import trevignano_2018 from '../js/trevignano2018.js';
import trevignano_2019 from '../js/trevignano2019.js';
import trevignano_2020 from '../js/trevignano2020.js';
import trevignano_2021 from '../js/trevignano2021.js';


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
      trevignano_2017: trevignano_2017,
      trevignano_2018: trevignano_2018,
      trevignano_2019: trevignano_2019,
      trevignano_2020: trevignano_2020,
      trevignano_2021: trevignano_2021,
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

      if (year == "2016") {
        this.month = "April"
        this.prophecies = this.trevignano_2016.filter(prophecy => {
        return prophecy.month_string.includes("April")
        })
      }
      else if (year == "2017") {
        this.month = "January"
        this.prophecies = this.trevignano_2017.filter(prophecy => {
        return prophecy.month_string.includes("January")
        })
      }
      else if (year == "2018") {
        this.month = "January"
        this.prophecies = this.trevignano_2018.filter(prophecy => {
        return prophecy.month_string.includes("January")
        })
      }

      else if (year == "2019") {
        this.month = "January"
        this.prophecies = this.trevignano_2019.filter(prophecy => {
        return prophecy.month_string.includes("January")
        })
      }

      else if (year == "2020") {
        this.month = "January"
        this.prophecies = this.trevignano_2020.filter(prophecy => {
        return prophecy.month_string.includes("January")
        })
      }

      else {
        this.month = "January"
        this.prophecies = this.trevignano_2021.filter(prophecy => {
        return prophecy.month_string.includes("January")
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
        this.prophecies = this.trevignano_2017.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })
      }
      else if (year == "2018") {
        this.prophecies = this.trevignano_2018.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })
      }

      else if (year == "2019") {
        this.prophecies = this.trevignano_2019.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })
      }

      else if (year == "2020") {
        this.prophecies = this.trevignano_2020.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })
      }
      else {
        this.prophecies = this.trevignano_2021.filter(prophecy => {
        return prophecy.month_string.includes(month)
        })

      }
    }
  },
  mounted () {
  },
  created() {
    this.getProphecies('2021', 'January')
  }
})



