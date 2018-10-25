/**
 * Created on 10/24/2018.
 */
var faker = require('faker')

let categories = []
for(let i = 1; i <= 10; i++) {
    let category = {
        id: i,
        name: faker.lorem.words()
    }
    categories.push(category)

}



module.exports = {
    categories:categories
}