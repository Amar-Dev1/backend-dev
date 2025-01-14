# 📑N-tier achitecture 
- its a system design pattern that structures an application into multiple logical layers or `tiers`
- each tier has a specific responsibility and communicates with the next tier using a well-defined interface

## Common Tiers in n-Tier Architecture
- **Application Tier**: This tier contains the core business logic of the application. It is responsible for Receiving and processing user requests
- **Presentation Tier**: This is the topmost layer where users interact with the application. It can be
a web interface, a mobile app, or a desktop application
- **Data Tier**: This tier is responsible for storing and managing data. It handles database operations like querying, updating, and deleting data.

### 💡Notes
- when these parts are in defferent places (defferent servers) => physical seperation  called `Tiers`.
- when these parts are in the same place (same server) => virtual seperation, called `Layers`.`
- the client machine called `Thin clients`, cuz they dont run bussines logic (only communicate with application and represent the data)

## 📑4-tier architecture
sometimes we have to add another tier. Whic is `Deliver Tier`:
- Responsible for deliver the data
- dael with `caching` and delivering frontend assets and `CDN`

## 💡 CDN
- Content Delivery Network
- a network of servers distributed across different geographic locations
- used to distribute content (like images, videos, and static assets) across the globe
- reduces latency and improves page load times by serving content from a server closer to the user's location