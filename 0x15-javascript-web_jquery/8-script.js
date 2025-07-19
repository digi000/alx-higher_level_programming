$(function () {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data, textStatus)
		{
			films = data.results
			for (const film of films) {
				$("UL#list_movies").append("<li>" + film.title + "</li>")
			}
		})
})
