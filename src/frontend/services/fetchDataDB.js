import { createClient } from "@libsql/client"
import { dbURL, dbAuthToken } from "./dbCredentials.js"

const db = createClient({
  url: dbURL,
  authToken: dbAuthToken 
})

export async function retrieveDBData(ageClass) {
  const query = await db.execute(`SELECT * FROM ${ageClass}`)
  return query.rows
}
