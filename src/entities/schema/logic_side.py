class Logic_side:
    @staticmethod
    def func_not(logic_objects: dict, now_obj: dict, queue_objects: list, random_id: int) -> bool:
        if len(now_obj["activated"]):
            now_obj["result_signal"] = False
        else:
            now_obj["result_signal"] = True
        obj_to_activate = logic_objects.get(str(now_obj["turn_object"]))
        if obj_to_activate:
            if now_obj["result_signal"]:
                obj_to_activate["activated"][str(random_id)] = True
            queue_objects.append(obj_to_activate)


    @staticmethod
    def func_splitter(logic_objects: dict, now_obj: dict, queue_objects: list, random_id: int) -> bool:
        if len(now_obj["activated"]):
            now_obj["result_signal"] = True
        else:
            now_obj["result_signal"] = False
        
        for maybe_id in now_obj["turn_object"]:
            obj_to_activate = logic_objects.get(str(maybe_id))
            if obj_to_activate:
                if now_obj["result_signal"]:
                    obj_to_activate["activated"][str(random_id)] = True
                    random_id += 1
                queue_objects.append(obj_to_activate)



    @staticmethod
    def func_node(logic_objects: dict, now_obj: dict, queue_objects: list, random_id: int) -> bool:
        if len(now_obj["activated"]):
            now_obj["result_signal"] = True
        else:
            now_obj["result_signal"] = False
        
        obj_to_activate = logic_objects.get(str(now_obj["turn_object"]))
        # print("---", obj_to_activate)
        if obj_to_activate:
            if now_obj["result_signal"]:
                obj_to_activate["activated"][str(random_id)] = True
            queue_objects.append(obj_to_activate)

    @staticmethod
    def func_and(logic_objects: dict, now_obj: dict, queue_objects: list, random_id: int) -> bool:
        if len(now_obj["activated"]) < 2:
            now_obj["result_signal"] = False
        elif len(now_obj["activated"]) > 2:
            print("BIG ERROR >2 activation 'add'")
            return
        else:
            b1, b2 = now_obj["activated"].values()
            now_obj["result_signal"] = b1 and b2

        obj_to_activate = logic_objects.get(str(now_obj["turn_object"]))
        # print("---", obj_to_activate)
        if obj_to_activate:
            if now_obj["result_signal"]:
                obj_to_activate["activated"][str(random_id)] = True
            queue_objects.append(obj_to_activate)

        

