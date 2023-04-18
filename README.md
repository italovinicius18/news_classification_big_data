# News classification with big data

Categorization of news through big data technologies for storage and machine learning

## Introduction

This project is a proof of concept of a news categorization system. The goal is to classify news in different categories. The system is composed of two parts: the first one is a web crawler that crawls news from different sources.

## Architecture

The architecture of the system is composed of the following components:

### News Crawler

The news crawler is a web crawler that crawls news from different sources and send them to a Kafka topic. The crawler is implemented in Python and uses the Scrapy framework.

#### News portals consumed

The following news portals are consumed by the crawler:

* G1 (http://g1.globo.com/)