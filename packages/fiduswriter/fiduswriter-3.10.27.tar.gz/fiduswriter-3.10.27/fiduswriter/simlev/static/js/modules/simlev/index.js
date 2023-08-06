export class PublishSimlev {
    constructor(publish) {
        this.publish = publish
    }

    init() {
        this.publish.publishUrl = "/proxy/simlev/publish_doc/"
    }
}
