#
# Copyright 2017 the original author or authors.
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
#


def initialize():
    global kafka_cluster_proxy_running, kafka_adapter_proxy_running, register_adapter_with_core 
    kafka_cluster_proxy_running = False
    kafka_adapter_proxy_running = False
    register_adapter_with_core = False

def readiness_probe():
    return kafka_cluster_proxy_running and kafka_adapter_proxy_running and register_adapter_with_core

def liveness_probe():
    return kafka_cluster_proxy_running and kafka_adapter_proxy_running and register_adapter_with_core
    
