import argentina_2021 from '../js/argentina2021.js';

import world_events from '../js/world_events.js';


new Vue({
  el: '#app',
  components: {


  },
  data () {
    return {
      error: null,
      resultCount: null,
      search: "",
      searchQuery: null,
      guidance: null,
      lang: "pl",
      keywordSearch: false,
      visitsCalendar: false,
      activeTopMenu: false,
      worldEvents: false,
      wordCloud: false,
      prophecies: [],
      messages: [],
      argentina_2021: argentina_2021,

      world_events: world_events,
    }
  },
  computed: {

  },
  methods: {
    setLanguage(lang) {
      this.lang = lang
    },
    setYear(year) {
      this.year = year;
      this.keywordSearch = false;
      this.visitsCalendar = false;
      this.worldEvents = false;
      this.month = "January"
      this.prophecies = this.argentina_2021.filter(prophecy => {
      return prophecy.month_string.includes("January")
      })
      document.getElementById('prophecyColumn').scrollTo(0,0);
    },
    getProphecies(year, month) {
      if (year == "2021") {
        this.prophecies = this.argentina_2021
      }
    },
  },
  mounted () {
  },
  created() {
    this.year = '2021'
    this.getProphecies(this.year)
  }
})


