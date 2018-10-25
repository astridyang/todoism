/**
 * Created on 10/24/2018.
 */
const Mock = require('mockjs')
const Random = Mock.Random
const domain = 'http://todoism.com/api';
const code = 200

const cateData = req => {
    let categories = []
    for(let i = 1; i <= 10; i++){
        let category = {
            id:i,
            name: Random.csentence(10, 25)
        }
        categories.push(category)
    }
    return {
        code,
        categories
    }
}

Mock.mock(`${domain}/categories`, 'get', cateData)