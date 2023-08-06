# Copyright 2020 The TensorStore Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load(
    "//third_party:repo.bzl",
    "third_party_http_archive",
)
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")
load("//:cmake_helpers.bzl", "cmake_add_dep_mapping", "cmake_fetch_content_package")

def repo():
    maybe(
        third_party_http_archive,
        name = "org_nghttp2",
        strip_prefix = "nghttp2-1.48.0",
        urls = [
            "https://github.com/nghttp2/nghttp2/releases/download/v1.48.0/nghttp2-1.48.0.tar.gz",
        ],
        sha256 = "66d4036f9197bbe3caba9c2626c4565b92662b3375583be28ef136d62b092998",
        build_file = Label("//third_party:org_nghttp2/bundled.BUILD.bazel"),
        system_build_file = Label("//third_party:org_nghttp2/system.BUILD.bazel"),
    )

# https://github.com/nghttp2/nghttp2/blob/master/CMakeLists.txt
cmake_fetch_content_package(name = "org_nghttp2")

cmake_add_dep_mapping(target_mapping = {
    "@org_nghttp2//:nghttp2": "nghttp2",
})
