# Changelog

## 0.6.0 (2026-04-28)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/linq-team/linq-python/compare/v0.5.0...v0.6.0)

### Features

* support setting headers via env ([d4398f4](https://github.com/linq-team/linq-python/commit/d4398f434cc4a920f59625eee7be9f1cdef8725b))


### Bug Fixes

* **openapi:** enforce mutual exclusivity constraints on reaction and voice memo schemas ([e057279](https://github.com/linq-team/linq-python/commit/e05727975ba84c6a022bd8e8d7a9d212cd864082))
* use correct field name format for multipart file arrays ([0e992dc](https://github.com/linq-team/linq-python/commit/0e992dc83b80f05698e9cc3d2e656f6ca890576a))

## 0.5.0 (2026-04-26)

Full Changelog: [v0.4.1...v0.5.0](https://github.com/linq-team/linq-python/compare/v0.4.1...v0.5.0)

### Features

* **api:** update docs link ([1a8c502](https://github.com/linq-team/linq-python/commit/1a8c502a622035274cff32f279f5781b8a9bab0e))

## 0.4.1 (2026-04-25)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/linq-team/linq-python/compare/v0.4.0...v0.4.1)

### Chores

* configure new SDK language ([196bf69](https://github.com/linq-team/linq-python/commit/196bf69450146c67bf2b82da2a64e70a71d2600b))

## 0.4.0 (2026-04-24)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/linq-team/linq-python/compare/v0.3.0...v0.4.0)

### Features

* make compliance webhooks (message.opt_out/opt_in) GA ([1a5b0e6](https://github.com/linq-team/linq-python/commit/1a5b0e6d75f47b67cb2447e180712d334f7f06d0))


### Documentation

* **api:** add first outbound message link restriction note to POST /v3/chats ([f44e698](https://github.com/linq-team/linq-python/commit/f44e6989ce805821306fb22c62a38c0f251c2846))

## 0.3.0 (2026-04-23)

Full Changelog: [v0.2.5...v0.3.0](https://github.com/linq-team/linq-python/compare/v0.2.5...v0.3.0)

### Features

* **api:** expose health_score on chats (BETA) ([b7d22d6](https://github.com/linq-team/linq-python/commit/b7d22d642e1192a77dd695c178eee322357de024))


### Chores

* **internal:** more robust bootstrap script ([b504bb9](https://github.com/linq-team/linq-python/commit/b504bb9f84501d3e20fe3654a67e739fa1986e77))

## 0.2.5 (2026-04-20)

Full Changelog: [v0.2.4...v0.2.5](https://github.com/linq-team/linq-python/compare/v0.2.4...v0.2.5)

### Documentation

* **api:** document edit message limits (BUG-7607) ([f7838ae](https://github.com/linq-team/linq-python/commit/f7838ae0fd6155e6db6cc501798c7c7665a63631))

## 0.2.4 (2026-04-18)

Full Changelog: [v0.2.3...v0.2.4](https://github.com/linq-team/linq-python/compare/v0.2.3...v0.2.4)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([0e5a821](https://github.com/linq-team/linq-python/commit/0e5a8217fcab667939e6a211e4f3b9abab7acfca))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([2d5ebac](https://github.com/linq-team/linq-python/commit/2d5ebacb793aa7f2f86b9e820db6e8f01b71605d))


### Documentation

* **openapi:** document typing indicator behavior and limitations ([3ea2cea](https://github.com/linq-team/linq-python/commit/3ea2ceaf47fd3a340a58e7334e58375f950862fc))

## 0.2.3 (2026-04-08)

Full Changelog: [v0.2.2...v0.2.3](https://github.com/linq-team/linq-python/compare/v0.2.2...v0.2.3)

### Bug Fixes

* **api-service:** add created_at and make sent_at nullable in SentMessage ([fa68395](https://github.com/linq-team/linq-python/commit/fa683950b661507844f9d1f22c4716daf9805810))
* block SMS group participant changes and fix e2e test failures ([e05f1af](https://github.com/linq-team/linq-python/commit/e05f1af36a6d37d13952bdad56f16b903bfccc34))

## 0.2.2 (2026-04-08)

Full Changelog: [v0.2.1...v0.2.2](https://github.com/linq-team/linq-python/compare/v0.2.1...v0.2.2)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([6c18c57](https://github.com/linq-team/linq-python/commit/6c18c57b5aa590fe7a096b98ef617f3be086d066))

## 0.2.1 (2026-04-07)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/linq-team/linq-python/compare/v0.2.0...v0.2.1)

### Bug Fixes

* add SVG support to synapse attachments ([c329c0a](https://github.com/linq-team/linq-python/commit/c329c0a19f398623d5035d1ff9e60375fc368f23))

## 0.2.0 (2026-04-04)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/linq-team/linq-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** config cleanup ([6827b8f](https://github.com/linq-team/linq-python/commit/6827b8f725103369b7588c47daf86368f5f3f8f0))

## 0.1.0 (2026-04-01)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/linq-team/linq-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** add python package ([1c8350d](https://github.com/linq-team/linq-python/commit/1c8350d60fecfea7afbc54268a4249238b2ef1cf))


### Chores

* configure new SDK language ([d9e49fb](https://github.com/linq-team/linq-python/commit/d9e49fb30147a79372eb95c1c0f5909e30f0ad79))
* update SDK settings ([b06339c](https://github.com/linq-team/linq-python/commit/b06339c582a977a2e5d7039687fbfdaf44841f7c))
* update SDK settings ([a969eea](https://github.com/linq-team/linq-python/commit/a969eea2ed010c55387c786702a36c4340084417))


### Documentation

* update contact card API docs with setup and sharing guidance ([37d3a46](https://github.com/linq-team/linq-python/commit/37d3a460564e68be034f53877c622e44822d1a24))
